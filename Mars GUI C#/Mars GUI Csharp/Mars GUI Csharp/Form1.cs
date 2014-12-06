using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }
    }
}
