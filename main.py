import typer
from typing import Optional
from pathlib import Path

app = typer.Typer()


@app.command('run')
def main(extension: str,
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequell cherché" ),
         delete: bool = typer.Option(False, help="Supprime les fichiers trouvés")):
    """
        Affiche les fichiers trouvés avec l'extension donnée.
    """

    if not directory:
        directory = Path.cwd()
    else:
        directory = Path(directory)


    if not directory.exists():
        typer.secho(f"Le dossier {directory} n'existe pas", fg=typer.colors.RED)
        raise typer.Exit()

    files = directory.rglob(f"*.{extension}")

    if delete:
        typer.confirm("Voulez vous vraiment supprimez les fichiers", abort=True)
        for file in files:
            file.unlink()
            typer.secho(file, fg=typer.colors.RED)
    else:
        typer.secho(f"fichiers trouvés avec l'extension {extension} :", fg=typer.colors.GREEN)
        for file in files:
            typer.secho(file, fg=typer.colors.GREEN)


@app.command('search')
def search(extension: str,
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequell cherché" ),
         delete: bool = typer.Option(False, help="Supprime les fichiers trouvés")):

    main(extension=extension, directory=directory, delete=False)
    

@app.command('delete')
def delete(extension: str,
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequell cherché" ),
         delete: bool = typer.Option(False, help="Supprime les fichiers trouvés")):
    
    main(extension=extension, directory=directory, delete=True)
