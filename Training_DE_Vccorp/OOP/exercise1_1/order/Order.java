package exercise1_1.order;

import exercise1_1.abstract_model.Customer;
import exercise1_1.customer.Manager;
import exercise1_1.customer.NonRegisteredCustomer;

import java.time.LocalDate; // import

public class Order {

    private LocalDate time;
    private boolean status;
    private final float amount;

    public Order(LocalDate time, boolean status, float amount) {
        this.time = time;
        this.status = status;
        this.amount = amount;
    }

    public void setTime(LocalDate time) {
        this.time = time;
    }

    public boolean isStatus() {
        return this.status;
    }

    public boolean getStatus() {
        return this.status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public LocalDate getTime() {
        return time;
    }

    public float caculateTax(Customer customer) {
        if (customer instanceof NonRegisteredCustomer ) {
            return amount * 10 / 100;
        }
        return amount * 1 / 100;
    }

    public float caculateTotal(Customer customer) {
        return caculateTax(customer) + amount;
    }
}
