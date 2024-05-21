//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.

        /*int num = 17;
        double num2 = 10.8;

        System.out.println("hello world");//

        String nome = "Luiz";
        System.out.println("Bem vindo "+nome);

        if (num > 10){
            System.out.println(("Maior que 10"));
        }
        else {System.out.println("Menor que 10");}

        for(int i = 0; i<10; i++){
            System.out.println(i);
        }*/

        Carro carro_1 = new Carro();
        carro_1.marca = "Fiat";
        carro_1.modelo = "Uno";
        carro_1.cor = "Cinza";
        carro_1.placa = "FDP-001";
        carro_1.ano = 1939;

       // System.out.println("O carro da marca " +carro_1.marca+" e modelo " +carro_1.modelo+", é do ano de " +carro_1.ano+" e possuí a placa " +carro_1.placa);
        carro_1.ligar();
        carro_1.desligar();
        carro_1.acelerar();
        carro_1.drif();


    }
}