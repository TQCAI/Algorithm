package tech_test;

import java.util.Date;

class Klass{
    static
    {
        System.out.println("类初始化");
    }
    Klass(){}
}

public class Main {
    public static void main(String[] args) {
        String all=String.join(",","A","B");
        System.out.println(all);
        System.out.println(new Date());
        Klass k1=new Klass();
        Klass k2=new Klass();
    }
}
