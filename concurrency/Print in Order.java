class Foo {
    
    private volatile boolean a = false;
    private volatile boolean b = false;


    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        a = !a;
    }

    public void second(Runnable printSecond) throws InterruptedException {
        while(!a){
            
        }
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        b = !b;
    }

    public void third(Runnable printThird) throws InterruptedException {
        while(!b){
            
        }
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}