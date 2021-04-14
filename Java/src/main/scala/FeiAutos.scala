class FeiAutos (var model:String, var make:String, var price:Int) {
  def finalPrice()={
    println(make+" Type:"+model+" Price is $"+price)
  }
  def student(price:Int)={price-3500}
  def enmployee(price:Int)={price-4600}
  def discount(f:Int=>Int,price:Int)={this.price=f(price)}

}

object Main{
  def main(args: Array[String]): Unit = {
    var car=new FeiAutos("RAV4","Toyota",37600)
    var auto=new FeiAutos("Focus","Ford",41200)
    var studentprice=(x:FeiAutos)=>x.discount(x.student,x.price)
    var employeeprice=(x:FeiAutos)=>x.discount(x.enmployee,x.price)
    studentprice(auto)
    employeeprice(car)
    auto.finalPrice()
    car.finalPrice()
  }
}