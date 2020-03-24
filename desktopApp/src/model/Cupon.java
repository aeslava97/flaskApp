package model;

public class Cupon {

	public String idUser;
	public String password;
	public int valueMoney;
	
	public Cupon(String idUser, String password, int valueMoney) {
		super();
		this.idUser = idUser;
		this.password = password;
		this.valueMoney = valueMoney;
	}
	public String getIdUser() {
		return idUser;
	}
	public void setIdUser(String idUser) {
		this.idUser = idUser;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public int getValueMoney() {
		return valueMoney;
	}
	public void setValueMoney(int valueMoney) {
		this.valueMoney = valueMoney;
	}
	
	
	
	
}
