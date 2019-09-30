package com.example.cropad;

public class marketdata {

    String marketName;
    String price;

    public marketdata(String marketName,String price){
        this.marketName=marketName;
        this.price=price;
    }

    public String getMarketName() {
        return marketName;
    }

    public void setMarketnName(String marketName) {
        this.marketName = marketName;
    }

    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
}
