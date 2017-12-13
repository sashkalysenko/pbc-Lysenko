from pbc.sg.sg import Grid, StartGrid
from pbc.sg.grid_console import GridConsole


def test_sel_grid(ssh):
    grid = StartGrid(Grid(ssh))
    grid.download()
    grid.download_node_config()
    grid.start_hub()
    grid.add_node()
    assert len(ssh.execute_command('pgrep java'))


def test_grid_console(firefox):
    grid_console = GridConsole(firefox)
    assert grid_console.get_amount_browsers() == grid_console.get_ammount_sessions()
