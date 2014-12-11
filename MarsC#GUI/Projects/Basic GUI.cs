using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        int prog = 0;
        Timer time1 = new Timer();
        //time1.start();

        public Form1()
        {
            InitializeComponent();
            //button1.Text = "Click Here";
            //button2.Text = "Don't click here";
            //button2.Enabled = false;
            //button3.Text = "Enter info";
            
            //label1.Text = "nothing";

            //button4.Text = "Close Window";
            //button5.Text = "stop";

            //label2.Text = "This is tab 1";
            //label3.Text = "This is tab 2";

            //tabPage1.Text = "Tab 1";
            //tabPage2.Text = "Tab 2";

            //label4.Text = "" + prog;
        }

        

      

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        

    }
}
//Text window like console on GUI
//Produce serial and interact with network
//  send UDP
//  receive UPD
//Joystick
//Panel receive video feed