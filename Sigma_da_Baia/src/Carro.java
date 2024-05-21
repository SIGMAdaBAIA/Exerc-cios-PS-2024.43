public class Carro {
     String marca;
     String modelo;
     String cor;
     String placa;
    int ano;

    boolean ligado = false;

    void ligar() {
        if (ligado == false) {
            ligado = true;
            System.out.println("Ligando");
        } else {
            System.out.println("O carro esta ligado!");
        }
    }
    void desligar(){
        if (ligado == true){
            ligado = false;
            System.out.println("Desligando");
        }
        else {
            System.out.println("Desligado");
        }
    }
    void drif(){
        if (ligado == true){
            System.out.println("Vruummmm!");
        }
        else {
            System.out.println("O carro esta desligado!");
        }
    }
    void acelerar() {
        if (ligado == true) {
            System.out.println("Acelerando");
        } else {
            System.out.println("O carro esta desligado!");
        }
    }
    void frear(){
        System.out.println("Freando");
    }
    void passar_macha(){
        System.out.println("Passando macha");
    }
    void ligar_farol() {
                System.out.println("Ligando farol");
        }
}