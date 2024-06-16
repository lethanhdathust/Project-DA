package exercise1_1.abstract_model;

import exercise1_1.order.Order;

import java.util.ArrayList;


public abstract class Customer {
     private String name;
     private String address;
     private int mobilePhone;
     private String email;
     protected ArrayList<Order> orders;
     public Customer(String name, String address, int mobilePhone, String email) {
          this.name = name;
          this.address = address;
          this.mobilePhone = mobilePhone;
          this.email = email;
     }
     public Customer() {
     }


     public abstract void buyOrder(Order order);
     public String getName() {
          return this.name;
     }

     public void setName(String name) {
          this.name = name;
     }

     public String getAddress() {
          return this.address;
     }

     public void setAddress(String address) {
          this.address = address;
     }

     public ArrayList<Order> getOrders() {
          return this.orders;
     }

     public void setOrders(ArrayList<Order> orders) {
          this.orders = orders;
     }


     public int getMobilePhone() {
          return mobilePhone;
     }

     public void setMobilePhone(int mobilePhone) {
          this.mobilePhone = mobilePhone;
     }

     public String getEmail() {
          return email;
     }

     public void setEmail(String email) {
          this.email = email;
     }

}
