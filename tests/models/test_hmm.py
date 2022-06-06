from virtool_core.models.hmm import HMMMinimal
import pytest


def test_hmm_model():
    """
    Tests the 'name' field validator for the
    `HMMMinimal` model

    """

    HMMMinimal(
        id="foo", cluster=899, count=45, families={"virus": 19}, name=["ryan", "blake"]
    )

    with pytest.raises(ValueError) as err:
        HMMMinimal(
            id="foo",
            cluster=899,
            count=45,
            families={"virus": 19},
            name=["john", "kelly", "tris", "ian"],
        )
        assert "The length of name should be a maximum of 3" in str(err)
