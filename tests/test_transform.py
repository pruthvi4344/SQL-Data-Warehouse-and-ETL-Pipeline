from etl.extract import extract_raw_data
from etl.transform import transform

def test_transform_outputs():
    data = extract_raw_data("data/raw")
    result = transform(data)
    assert "fact_sales" in result
    assert len(result["fact_sales"]) > 0
