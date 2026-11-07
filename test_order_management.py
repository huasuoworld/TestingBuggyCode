import pytest
from .order_management import Order

@pytest.fixture
def mock_order():
    return Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])

def test_calculate_total(mock_order):
    total = mock_order.calculate_total()
    #calculate total price
    total_price = 2*15.00 + 5*1.50
    print(f"total is {total}, total_price is {total_price}")
    assert total == total_price

def test_apply_discount(mock_order):
    discount = mock_order.apply_discount("SAVE30")
    print(f"discount SAVE30 is {discount}")
    assert discount is not None

def test_add_item(mock_order):
    mock_order.add_item("Notebook", 3, 5.00)

def test_remove_item(mock_order):
    mock_order.remove_item("Pen")

def test_print_summary(mock_order):
    mock_order.print_summary()

def test_integration1(mock_order):
    mock_order.add_item("Notebook", "3", 5.00)
    mock_order.remove_item("Pen")
    total = mock_order.calculate_total()
    discount = mock_order.apply_discount("SAVE10")
    final_total = total * (1 - discount)
    print(f"Integration test - total: {total}, discount: {discount}, final_total: {final_total}")
    assert total > 0
    assert discount == 0.1

def test_integration2(mock_order):
    mock_order.add_item("Notebook", 3, "5.00")
    mock_order.remove_item("Pen")
    total = mock_order.calculate_total()
    discount = mock_order.apply_discount("SAVE10")
    final_total = total * (1 - discount)
    print(f"Integration test - total: {total}, discount: {discount}, final_total: {final_total}")
    assert total > 0
    assert discount == 0.1

