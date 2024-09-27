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
        input = ""
        while True:
            temp = sys.stdin.readline()
            if not temp:
                break # EOF
            input += temp
    except KeyboardInterrupt:
        pass  # Handle any cleanup here if necessary
    pyperclip.copy (input)

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