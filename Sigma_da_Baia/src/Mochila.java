import javax.swing.*;

public class Mochila {
    public String marca;
    public String modelo;
    public String cor;
    public String categoria;
    public String tema;

    public Mochila(String marca, String modelo, String cor, String categoria, String tema) {
        setMarca(marca);
        setModelo(modelo);
        setCor(cor);
        setCategoria(categoria);
        setTema(tema);
    }

    public void setMarca(String marca) {
        this.marca = marca;
        System.out.println("A marca da mochila foi setada");
    }
    public String getMarca(){
        return this.marca ;
    }
    public void setModelo(String modelo){
        this.marca = modelo;
        System.out.println("O modelo da mochila foi setada");
    }
    public String getModelo(){
        return this.modelo;
    }
    public void setCor(String cor){
        this.marca = cor;
        System.out.println("A cor da mochila foi setada");
    }
    public String getCor(){
        return this.cor;
    }
    public void setCategoria(String categoria){
        this.categoria = categoria;
        System.out.println("A Categotia da mochila foi setada");
    }
    public String getCategoria(){
        return this.categoria;
    }
    public void setTema(String tema){
        this.tema = tema;
        System.out.println("O Tema da mochila foi setada");
    }
    public String getTema(){
        return this.tema;
    }

    boolean abrir = false;

    void abrir(){
        if (abrir == false) {
            abrir = true;
            System.out.println("Abrindo mochila");
        } else {
            System.out.println("A mochila esta aberta");
        }
    }
    void fechar(){
        if (abrir == true) {
            abrir = false;
            System.out.println("Fechando mochila");
        }
        else {
            System.out.println("A mochila ja esta fechada");
        }
    }
    void    guarda(){
        System.out.println("Guardando objetos na mochila");
    }
    void    locomover(){
        System.out.println("Levar a mochila para outro lugar");
    }
}
