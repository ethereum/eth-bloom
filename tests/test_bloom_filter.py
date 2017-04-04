from hypothesis import (
    strategies as st,
    given,
)
from eth_bloom import (
    BloomFilter,
)


address = st.binary(min_size=20, max_size=20)
topic = st.binary(min_size=32, max_size=32)
topics = st.lists(topic, min_size=0, max_size=4)


log_entry = st.tuples(address, topics)
log_entries = st.lists(log_entry, min_size=0, max_size=30)


@given(log_entries)
def test_bloom_filter(log_entries):
    bloom = BloomFilter()

    for address, topics in log_entries:
        bloom.add(address)
        for topic in topics:
            bloom.add(topic)

    for address, topics in log_entries:
        assert address in bloom
        for topic in topics:
            assert topic in bloom
