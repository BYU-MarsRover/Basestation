using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Net.Sockets;
using System.Net;

namespace Mars_GUI_Csharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            label1.Text = "X: 00000.00";
            label2.Text = "Y: 00000.00";
            label3.Text = "Z: 00000.00";
            label4.Text = "Status:  Good";
            label5.Text = "HP:  100";
            label6.Text = "HAL the Rover";
            label7.Text = "Battery condition:  _______";
            label8.Text = "Extra cameras/sources";
            checkBox1.Text = "Send";
            checkBox2.Text = "Receive";

            //implement send/receive boxes to toggle when sending/receiving data
            //implement a console to display info, like contents of UDP packets
            //implement steaming video feed
            //labels for sensor data
            //visual to track joystick

            //code snippit from http://stackoverflow.com/questions/12864999/sending-and-receiving-udp-packets
            //The following code sends a packet on port 15000:
            int port = 15000;
            UdpClient udp = new UdpClient();
            //udp.EnableBroadcast = true;  //This was suggested in a now deleted answer
            IPEndPoint groupEP = new IPEndPoint(IPAddress.Broadcast, port);
            string str4 = "I want to receive this!";
            byte[] sendBytes4 = Encoding.ASCII.GetBytes(str4);
            udp.Send(sendBytes4, sendBytes4.Length, groupEP);
            checkBox1.Checked = true;
            udp.Close();
            //

            //Display UDP packets
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }
    }
}
