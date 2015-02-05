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
            button1.Text = "Send upd packet";
            button2.Text = "my new button";
            button2.SetBounds(200, 300, 200, 100);
            button2.Enabled = true;

            //implement send/receive image to toggle when sending/receiving data
            //implement a console to display info, like contents of UDP packets
            //implement steaming video feed
            //labels for sensor data
            //visual to track joystick

            //Receive udp packets

            //Following code from: http://stackoverflow.com/questions/12864999/sending-and-receiving-udp-packets
            //Server
            /*IPEndPoint ServerEndPoint= new IPEndPoint(IPAddress.Any,9050);
            Socket WinSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
            WinSocket.Bind(ServerEndPoint);
            Console.Write("Waiting for client");
            IPEndPoint sender = new IPEndPoint(IPAddress.Any, 0);
            EndPoint Remote = (EndPoint)(sender);
            int recv = WinSocket.ReceiveFrom(data, ref Remote);
            Console.WriteLine("Message received from {0}:", Remote.ToString());
            Console.WriteLine(Encoding.ASCII.GetString(data, 0, recv));
            */
            //Client
            /*IPEndPoint RemoteEndPoint= new IPEndPoint(IPAddress.Parse("ServerHostName"), 9050);
            Socket server = new Socket(AddressFamily.InterNetwork,SocketType.Dgram, ProtocolType.Udp);
            string welcome = "Hello, are you there?";
            byte[] data = Encoding.ASCII.GetBytes(welcome);
            server.SendTo(data, data.Length, SocketFlags.None, RemoteEndPoint);
            */
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //code snippit from http://stackoverflow.com/questions/12864999/sending-and-receiving-udp-packets
            //The following code sends a packet on the specified port
            int port = 27015;
            UdpClient udp = new UdpClient();
            IPEndPoint groupEP = new IPEndPoint(IPAddress.Broadcast, port);
            string str4 = "Message sent...";
            byte[] sendBytes4 = Encoding.ASCII.GetBytes(str4);
            udp.Send(sendBytes4, sendBytes4.Length, groupEP);
            udp.Close();
            //
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

    }
}
