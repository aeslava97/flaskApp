package controller;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

import com.google.gson.Gson;

import model.Cupon;

public class Controller {

	
	public static int httpRequest(Cupon cupon) throws IOException {
		Gson gson = new Gson();
		System.out.println(gson.toJson(cupon));
		
		
		URL url = new URL("http://localhost:5000/receiveCupon");
		HttpURLConnection con = (HttpURLConnection) url.openConnection();
		con.setRequestProperty("Content-Type", "application/json; utf-8");
		con.setRequestMethod("POST");
		con.setConnectTimeout(5000);
		con.setReadTimeout(5000);
		con.setDoOutput(true);
		
		try(OutputStream os = con.getOutputStream()) {
		    byte[] input = gson.toJson(cupon).getBytes("utf-8");
		    os.write(input, 0, input.length);           
		}

		int status = con.getResponseCode();
		System.out.println(status);

		return status;
	}
}
