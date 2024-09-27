import typer
import sys
import pyperclip

app = typer.Typer(help="pb: A Copy/paste CLI utility.")

@app.command()
def copy():
    """
    Write to your clipboard the content from STDIN
    """
    try:
        while True:
            input = sys.stdin.readline()
            if not input:
                break # EOF
            pyperclip.copy (input)
    except KeyboardInterrupt:
        pass  # Handle any cleanup here if necessary 

@app.command()
def paste():
    """
    Write to STDOUT the contents of your clipboard
    """
    output = pyperclip.paste()
    sys.stdout.write(output)
    sys.stdout.flush()

if __name__ == "__main__":
    app()