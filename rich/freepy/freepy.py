from subprocess import run, PIPE
from rich.console import Console
from rich.table import Table

console = Console()

try:
    r = run(['free','-h'], stdout=PIPE)

    rows = r.stdout.__repr__().split('\\n')[0].split()
    memory = r.stdout.__repr__().split('\\n')[1].split()
    swapmemory = r.stdout.__repr__().split('\\n')[2].split()
    rows[0] = ""

    table = Table(show_header=True, header_style="bold cyan", show_lines=True)

    for i in rows:
        table.add_column(i)

    table.add_row("[bold yellow]""Mem:""[/bold yellow]",memory[1],"[bold red]"+memory[2]+"[/bold red]","[bold green]"+memory[3]+"[/bold green]",memory[4],memory[5],memory[6])
    table.add_row("[bold yellow]""Swap:""[/bold yellow]",swapmemory[1],swapmemory[2],swapmemory[3])

    console.print(table)
    
except Exception as e:
    print(f"Error in printing memory - {e}")