import click
import requests
# a command line tool to download a file from a URL
# then copy that file and rename to a chosen name into sprites/dex, sprites/ani and sprites/gen5
# then if the back option is true, add -back to the directories and if the shiny option is true, add -shiny to the directories
# do not add -back for dex

@click.command()
@click.option('--url', prompt='URL', help='The URL of the image to download.')
@click.option('--name', prompt='Name', help='The name of the sprite.')
@click.option('--back', default=False, help='Whether the sprite is a back sprite.')
@click.option('--shiny', default=False, help='Whether the sprite is a shiny sprite.')
def add_sprite(url, name, back, shiny):
    for directory in ['dex', 'ani', 'gen5']:
        if back and directory != 'dex':
            directory += '-back'
        if shiny:
            directory += '-shiny'
        r = requests.get(url, allow_redirects=True)
        open(f'sprites/{directory}/{name}', 'wb').write(r.content)

if __name__ == '__main__':
    add_sprite()