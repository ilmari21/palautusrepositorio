from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    console = Console()
    season = Prompt.ask("Season", choices=["2023-24", "2024-25", "2025-26", "2026-27"])
    stats = create_stats(season)
    run_queries(console, stats, season)


def run_queries(console, stats, season):
    while True:
        search_type = ask_search_type()
        if search_type is None:
            break

        result = search_players(stats, search_type)
        if result is None:
            break
        players, value = result
        table = create_table(players, value, season)
        console.print(table)


def create_stats(season):
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    return PlayerStats(PlayerReader(url))


def ask_search_type():
    search_type = Prompt.ask(
        "Search by (q to quit)",
        choices=["nationality", "team", "q"],
        case_sensitive=False,
    )
    if search_type.lower() == "q":
        return None

    return search_type.lower()


def search_players(stats, search_type):
    if search_type == "nationality":
        value = ask_nationality()
        if value is None:
            return None
        return stats.top_scorers_by_nationality(value), value

    value = ask_team()
    if value is None:
        return None
    return stats.top_scorers_by_team(value), value


def ask_nationality():
    nationality = Prompt.ask(
        "Nationality (q to quit)",
        choices=["USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SVN", "FRA", "GBR", "SVK",
                 "DNK", "NED", "AUT", "BLR", "GER", "CHE", "NOR", "UZB", "LAT", "AUS", "q"],
        case_sensitive=False,
    )
    if nationality.lower() == "q":
        return None

    return nationality.upper()


def ask_team():
    team = Prompt.ask("Team abbreviation (q to quit)")
    if team.lower() == "q":
        return None

    return team.upper()


def create_table(players, value, season):
    table = Table(title=f"Top scorers from {value} ({season})")
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

    return table

if __name__ == "__main__":
    main()
