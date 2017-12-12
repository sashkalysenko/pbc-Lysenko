from pbc.sg.sg import Grid, StartGrid


def test_sel_grid(ssh):
    grid = StartGrid(Grid(ssh))
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert len(ssh.execute_command('pgrep java'))
