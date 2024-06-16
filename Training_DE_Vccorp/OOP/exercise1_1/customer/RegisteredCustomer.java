package exercise1_1.customer;


import exercise1_1.abstract_model.Customer;
import exercise1_1.interfaces.User;
import exercise1_1.order.Order;

public class RegisteredCustomer extends Customer implements User {

    public RegisteredCustomer(String name, String address, int mobilePhone , String email) {
        super(name, address, mobilePhone, email);
        //TODO Auto-generated constructor stub
    }

    public RegisteredCustomer() {
        super();
    }

    @Override
    public void buyOrder(Order order) {
        float amount = order.caculateTotal(this);
        super.orders.add(order);
        System.out.println("The amount for the register customer's bill" + amount
        );
    }

    @Override
    public void generateReceipt(Order order) {
        System.out.println("The status of the order" + order.isStatus() + " " +"Time " + order.getTime() + "Amount " + order.caculateTotal(this));
    }


}
