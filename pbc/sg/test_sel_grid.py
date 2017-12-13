from pbc.sg.sg import Grid, StartGrid
from pbc.sg.grid_console import GridConsole
from pbc.sg.python_org import PythonOrg


def test_sel_grid(ssh):
    grid = StartGrid(Grid(ssh))
    grid.download()
    grid.download_node_config()
    grid.start_hub()
    grid.add_node()
    assert len(ssh.execute_command('pgrep java')) == 2


def test_grid_console(firefox):
    grid_console = GridConsole(firefox)
    assert grid_console.get_amount_browsers() == grid_console.get_ammount_sessions()


def test_remote_driver(remote_ff):
    try:
        python_org = PythonOrg(remote_ff)
        python_org.save_screenshot('python.png')
        assert 'Python' in python_org.driver.title
        python_org.search_for("pycon")
        python_org.save_screenshot('pycon.png')
        python_org.open_home_page()
    except Exception as a:
        print a.message
        raise a
    finally:
        print 'close'
