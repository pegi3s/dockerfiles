#@title 🧬 Alanine Scanning Mutagenesis (Trim & Stop on Overlap) { display-mode: "form" }
#@markdown > Sliding window alanine replacement stops after first trimmed substitution.

import os
from ipywidgets import Textarea, IntText, Button, Layout, HBox, Output
from IPython.display import display, Markdown
try:
    from google.colab import files
    is_colab = True
except ImportError:
    is_colab = False

filename = "/content/alanine_scanned_sequences.fasta"

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

def generate_alanine_scans(fasta_text, window_size, stride):
    if window_size < 2:
        raise ValueError("Window size must be at least 2.")
    if stride < 1:
        raise ValueError("Stride must be at least 1.")

    parsed = parse_fasta(fasta_text)
    result = []
    for header, sequence in parsed:
        seq_len = len(sequence)
        for i in range(0, seq_len, stride):
            remaining = seq_len - i
            if remaining <= 0:
                break
            actual_window = min(window_size, remaining)
            modified = sequence[:i] + "A" * actual_window + sequence[i + actual_window:]
            result.append(f"{header}_AlaScan{i+1}\n{modified}")
            if actual_window < window_size:
                break  # Stop after first trimming event
    return "\n".join(result)

# Input Widgets
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
    description="Window size (≥2):",
    style={'description_width': 'initial'},
    layout=Layout(margin='10px 0px 10px 0px')
)

stride_input = IntText(
    value=3,
    description="Stride:",
    style={'description_width': 'initial'},
    layout=Layout(margin='10px 0px 10px 0px')
)

output_area = Output()
download_button = Button(
    description="Download Alanine FASTA",
    layout=Layout(width='auto', margin='0px 0px 0px 50px'),
    button_style='success',
    disabled=True
)

def on_generate_clicked(b):
    output_area.clear_output()
    download_button.disabled = True

    with output_area:
        try:
            window = int(window_size_input.value)
            stride = int(stride_input.value)
            scanned = generate_alanine_scans(fasta_input.value, window, stride)
            display(Markdown(f"### Alanine-Scanned Sequences\n```\n{scanned}\n```"))

            with open(filename, "w") as f:
                f.write(scanned)

            download_button.disabled = False
        except Exception as e:
            print(f"Error: {e}")

def on_download_clicked(b):
    if is_colab and os.path.exists(filename):
        files.download(filename)

generate_button = Button(
    description="Generate Alanine Variants",
    button_style='primary',
    layout=Layout(width='auto')
)
generate_button.on_click(on_generate_clicked)
download_button.on_click(on_download_clicked)

button_row = HBox([generate_button, download_button],
                  layout=Layout(justify_content='flex-start'))

display(fasta_input, window_size_input, stride_input, button_row, output_area)

import argparse
import sys

if __name__ == "__main__":
    # Check if we are in a terminal (not in a notebook/widget environment)
    if not sys.stdin.isatty() or len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Alanine Scanning Mutagenesis")
        parser.add_argument("--window", type=int, default=10, help="Window size")
        parser.add_argument("--stride", type=int, default=3, help="Stride size")
        parser.add_argument("--input", type=str, help="Path to FASTA file")
        
        args = parser.parse_args()

        # Get the sequence data
        if args.input and os.path.exists(args.input):
            with open(args.input, 'r') as f:
                fasta_data = f.read()
        else:
            # Default to the example if no file provided
            fasta_data = fasta_input.value 

        # Run the actual logic function
        results = generate_alanine_scans(fasta_data, args.window, args.stride)
        
        # Output to terminal or file
        print(results)
        with open("output.fasta", "w") as f:
            f.write(results)
        print("\n--- Results saved to output.fasta ---")
    else:
        # If no arguments, try to show the widgets (for Notebooks)
        display(fasta_input, window_size_input, stride_input, button_row, output_area)
