def test_import_and_version():
    import eth_bloom

    assert isinstance(eth_bloom.__version__, str)
