from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    console = Console()
    season = Prompt.ask("Season", choices=["2023-24", "2024-25", "2025-26"])

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = Prompt.ask(
            "Nationality (q to quit)",
            choices=["USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR", "SVK",
                     "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS", "q"],
            case_sensitive=False,
        )
        if nationality.lower() == "q":
            break

        nationality = nationality.upper()
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top scorers from {nationality} ({season})")
        table.add_column("Player", style="cyan")
        table.add_column("Team(s)", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="green")

        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.points),
            )

        console.print(table)

if __name__ == "__main__":
    main()
