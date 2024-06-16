package exercise1_1.customer;

import exercise1_1.abstract_model.Customer;
import exercise1_1.interfaces.User;
import exercise1_1.order.Order;

public class Manager extends Customer implements User {
    private static int numberCountOfOrder = 0;


    public Manager(String name, String address, int mobilePhone, String email) {
        super(name, address, mobilePhone, email);
    }

    public Manager() {
    }

    public static int getNumberCountOfOrder() {
        return numberCountOfOrder;
    }


    @Override
    public void buyOrder(Order order) {
        float amount = order.caculateTotal(this);
        super.orders.add(order);
        System.out.println("The amount for the manager's bill" + amount
        );
        numberCountOfOrder++;
    }

    @Override
    public void generateReceipt(Order order) {
        System.out.println("The status of the order" + order.isStatus() + " " +"Time " + order.getTime() + "Amount " + order.caculateTotal(this));
    }
}
