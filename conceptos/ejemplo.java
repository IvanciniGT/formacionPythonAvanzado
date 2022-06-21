public class Rectangulo{
    
    private int base;
    private int altura;
    
    public Rectangulo(int base, int altura){
        this.base=base;
        setAltura(altura);
    }
    public int getBase(){
        return this.base;
    }
    public int getAltura(){
        return this.altura;
    }
    public void setBase(int base){
        this.base=base;
    }
    public void setAltura(int altura){
        if(altura<0) throw new Exception ("Base no admitida");
        this.altura=altura;
    }
    public int getPerimetro(){
        return (this.base+this.altura)*2;
    }
    public int getArea(){
        return (this.base*this.altura);
    }
    
}
////// Legiones de personas escribiendo este tipo de codigo
Rectangulo gulo=new Rectangulo(1,4)
System.out.println(gulo.getBase())

