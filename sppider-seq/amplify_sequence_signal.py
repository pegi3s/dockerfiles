#@title 🧬 Sequence Signal Amplification { display-mode: "form" }
#@markdown > Extracts a sequence window of fixed size and appends it to the C-terminus of the original sequence using a sliding window with a fixed stride.

import os
from ipywidgets import Textarea, IntText, Button, Layout, HBox, Output
from IPython.display import display, Markdown
try:
    from google.colab import files
    is_colab = True
except ImportError:
    is_colab = False

filename = "/content/window_appended_sequences.fasta"

# --- FASTA Parser ---
def parse_fasta(text):
    sequences = []
    header = None
    seq_lines = []
    for line in text.strip().splitlines():
        line = line.strip()
        if line.startswith(">"):
            if header and seq_lines:
                sequences.append((header, ''.join(seq_lines)))
            header = line
            seq_lines = []
        else:
            seq_lines.append(line)
    if header and seq_lines:
        sequences.append((header, ''.join(seq_lines)))
    return sequences

# --- Windowed Appending Logic ---
def generate_appended_window_scans(fasta_text, window_size, stride):
    if window_size < 3:
        raise ValueError("Window size must be at least 3.")
    if stride < 1:
        raise ValueError("Stride must be at least 1.")

    parsed = parse_fasta(fasta_text)
    result = []

    for header, sequence in parsed:
        seq_len = len(sequence)

        for i in range(0, seq_len, stride):
            if i + window_size > seq_len:
                break  # Stop before trimmed (partial) window

            window = sequence[i:i + window_size]
            modified = sequence + window
            result.append(f"{header}_WinApp{i+1}\n{modified}")

    return "\n".join(result)

# --- UI Widgets ---
fasta_input = Textarea(
    value="""
>Example1
MTMTLHTKASGMALLHQIQGNELEPLNRPQLKIPLERPLGEVYLDSSKPAVYNYPEGAAY
>Example2
MVEIFDMLLATSSRFRMMNLQGEEFVCLKSIIL
""",
    placeholder="Paste FASTA-formatted sequences here",
    description="FASTA Input:",
    layout=Layout(width="80%", height="200px"),
    style={'description_width': 'initial'}
)

window_size_input = IntText(
    value=10,
    description="Window size (≥3):",
    style={'description_width': 'initial'},
    layout=Layout(margin='10px 0px 10px 0px')
)

stride_input = IntText(
    value=5,
    description="Stride:",
    style={'description_width': 'initial'},
    layout=Layout(margin='10px 0px 10px 0px')
)

output_area = Output()
download_button = Button(
    description="Download Appended FASTA",
    layout=Layout(width='auto', margin='0px 0px 0px 50px'),
    button_style='success',
    disabled=True
)

# --- Button Logic ---
def on_generate_clicked(b):
    output_area.clear_output()
    download_button.disabled = True

    with output_area:
        try:
            window = int(window_size_input.value)
            stride = int(stride_input.value)
            scanned = generate_appended_window_scans(fasta_input.value, window, stride)
            display(Markdown(f"### Appended Sequences\n```\n{scanned}\n```"))

            with open(filename, "w") as f:
                f.write(scanned)

            download_button.disabled = False
        except Exception as e:
            print(f"Error: {e}")

def on_download_clicked(b):
    if is_colab and os.path.exists(filename):
        files.download(filename)

generate_button = Button(
    description="Generate Appended Variants",
    button_style='primary',
    layout=Layout(width='auto')
)
generate_button.on_click(on_generate_clicked)
download_button.on_click(on_download_clicked)

button_row = HBox([generate_button, download_button],
                  layout=Layout(justify_content='flex-start'))

# --- Display ---
display(fasta_input, window_size_input, stride_input, button_row, output_area)

