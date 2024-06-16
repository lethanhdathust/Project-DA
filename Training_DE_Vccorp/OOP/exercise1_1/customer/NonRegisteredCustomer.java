package exercise1_1.customer;

import exercise1_1.abstract_model.Customer;
import exercise1_1.order.Order;

public class NonRegisteredCustomer extends Customer {



    public NonRegisteredCustomer(String name, String address, int mobilePhone, String email) {
        super(name, address, mobilePhone, email);
        //TODO Auto-generated constructor stub
    }

    public NonRegisteredCustomer() {
        super();
    }

    @Override
    public void buyOrder(Order order) {
        float amount = order.caculateTotal(this);
        super.orders.add(order);
        System.out.println("The amount for the non-register customer 's bill" + amount
        );
    }



}
