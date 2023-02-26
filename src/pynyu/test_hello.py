from pynyu.hello import hello_world


def test_output(capfd):
    hello_world()
    out, err = capfd.readouterr()
    assert out == "hello\n"
