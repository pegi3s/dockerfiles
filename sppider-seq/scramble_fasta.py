#@title ⚙️ FASTA scrambler { display-mode: "form" }
#@markdown > Scramble the input sequence(s) a given number of times.

import os
import random
import ipywidgets as widgets
from IPython.display import display, Markdown
from ipywidgets import HBox, Layout

try:
    from google.colab import files
    is_colab = True
except ImportError:
    is_colab = False

# Save output here for Colab compatibility
filename = "/content/scrambled_sequences.fasta"

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

def scramble_sequence(seq):
    scrambled = list(seq)
    random.shuffle(scrambled)
    return ''.join(scrambled)

def generate_scrambled_sequences(fasta_text, num_scrambles):
    parsed = parse_fasta(fasta_text)
    result = []
    for header, sequence in parsed:
        for i in range(num_scrambles):
            scrambled = scramble_sequence(sequence)
            result.append(f"{header}_scramble{i+1}\n{scrambled}")
    return "\n".join(result)

# Widgets
fasta_input = widgets.Textarea(
    value="""
>Example1
MTMTLHTKASGMALLHQIQGNELEPLNRPQLKIPLERPLGEVYLDSSKPAVYNYPEGAAY
>Example2
MVEIFDMLLATSSRFRMMNLQGEEFVCLKSIIL
""",
    placeholder="Paste FASTA-formatted sequences here",
    description="FASTA Input:",
    layout=widgets.Layout(width="80%", height="200px"),
    style={'description_width': 'initial'}
)

num_scrambles_input = widgets.IntText(
    value=3,
    description="Scrambles per sequence:",
    style={'description_width': 'initial'},
    layout=widgets.Layout(margin='20px 0px 20px 0px')
)

output_area = widgets.Output()
download_button = widgets.Button(
    description="Download Scrambled FASTA",
    layout=widgets.Layout(width='auto', margin='0px 0px 0px 50px'),
    button_style='success',
    disabled=True)

def on_generate_clicked(b):
    output_area.clear_output()
    download_button.disabled = True

    with output_area:
        try:
            num_scrambles = int(num_scrambles_input.value)
            if num_scrambles <= 0:
                raise ValueError("Number of scrambles must be positive.")
            scrambled = generate_scrambled_sequences(fasta_input.value, num_scrambles)
            display(Markdown(f"### Scrambled Sequences\n```\n{scrambled}\n```"))

            # Save to file
            with open(filename, "w") as f:
                f.write(scrambled)

            download_button.disabled = False
        except Exception as e:
            print(f"Error: {e}")

def on_download_clicked(b):
    if is_colab and os.path.exists(filename):
        files.download(filename)

generate_button = widgets.Button(
    description="Generate Scrambled Sequences",
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='auto', margin='0px 0px 0px 0px'),
    button_style='primary'
)
generate_button.on_click(on_generate_clicked)
download_button.on_click(on_download_clicked)

button_row = HBox([generate_button, download_button],
                  layout=Layout(justify_content='flex-start'))

display(fasta_input, num_scrambles_input, button_row, output_area)

