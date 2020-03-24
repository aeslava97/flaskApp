package view;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import java.awt.BorderLayout;
import javax.swing.JButton;
import javax.swing.SwingConstants;

import controller.Controller;
import model.Cupon;

import java.awt.event.ActionListener;
import java.io.IOException;
import java.awt.event.ActionEvent;
import java.awt.Color;
import javax.swing.JLabel;

public class Home {

	private JFrame frame;
	private JTextField txtInsertValueOf;
	private JButton btnNewButton = new JButton("create cupon");
	private JLabel lblNewLabel = new JLabel("Insert value of cupon");
	private final JLabel lblNewLabel_1 = new JLabel("Email");
	private final JTextField emailtxtFIeld = new JTextField();
	private final JLabel lblNewLabel_2 = new JLabel("Password");
	private final JTextField passwordTextField = new JTextField();
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Home window = new Home();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Home() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		passwordTextField.setBounds(154, 56, 180, 20);
		passwordTextField.setColumns(10);
		emailtxtFIeld.setBounds(154, 31, 180, 20);
		emailtxtFIeld.setColumns(10);
		frame = new JFrame();
		frame.setBounds(100, 100, 360, 170);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		txtInsertValueOf = new JTextField();
		txtInsertValueOf.setForeground(new Color(0, 0, 0));
		txtInsertValueOf.setBackground(new Color(255, 255, 255));
		txtInsertValueOf.setToolTipText("");
		txtInsertValueOf.setBounds(154, 6, 180, 20);
		frame.getContentPane().add(txtInsertValueOf);
		txtInsertValueOf.setColumns(10);
		
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				try {
					Cupon cupon = new Cupon(emailtxtFIeld.getText(), passwordTextField.getText(),Integer.parseInt((txtInsertValueOf.getText())));
					int rta = Controller.httpRequest(cupon);
					if (rta != 204) {
						JOptionPane.showMessageDialog(frame, "incorrect user or password","Warning",JOptionPane.ERROR_MESSAGE);
					}
				}catch (NumberFormatException e2) {
					JOptionPane.showMessageDialog(frame, "Incorrect formatting","Warning",JOptionPane.ERROR_MESSAGE);
				} 
				catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
			}
		});
		btnNewButton.setBackground(new Color(255, 255, 255));
		btnNewButton.setBounds(106, 97, 95, 23);
		frame.getContentPane().add(btnNewButton);
		
		
		lblNewLabel.setBounds(11, 9, 136, 14);
		frame.getContentPane().add(lblNewLabel);
		lblNewLabel_1.setBounds(11, 34, 46, 14);
		
		frame.getContentPane().add(lblNewLabel_1);
		
		frame.getContentPane().add(emailtxtFIeld);
		lblNewLabel_2.setBounds(11, 59, 46, 14);
		
		frame.getContentPane().add(lblNewLabel_2);
		
		frame.getContentPane().add(passwordTextField);
	}
}