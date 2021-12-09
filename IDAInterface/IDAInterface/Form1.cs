using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.Diagnostics;

using System.Drawing.Drawing2D;
namespace IDAInterface
{
    public partial class Form1 : Form
    {
        [DllImport("Gdi32.dll", EntryPoint = "CreateRoundRectRgn")]
        private static extern IntPtr CreateRoundRectRgn
        (
            int nLeftRect,
            int nTopRect,
            int nRightRect,
            int nBottomRect,
            int nWidthEllipse,
            int nHeightEllipse
        );

        bool on = true;

        public Form1()
        {
            InitializeComponent();
            //this.FormBorderStyle = FormBorderStyle.None;
            this.Region = Region.FromHrgn(CreateRoundRectRgn(0, 0, this.Width, this.Height, 30, 30));
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void btnIniciarDetener_Click(object sender, EventArgs e)
        {
            Process proceso = new Process();
            

            if(rdbManual.Checked == true && on ==true)
            {
                proceso.StartInfo.FileName = @"C:\Program Files (x86)\IDA\rougue-studios\IDA\scripts\ida.py";
                proceso.Start();
                
            }
            
            if (rdbAutomatico.Checked == true && on == true)
            {
                proceso.StartInfo.FileName = @"C:\Program Files (x86)\IDA\rougue-studios\IDA\scripts\ida_automatico.py";
                proceso.Start();
                
            }
         
            if (rdbSiempreEscuchando.Checked == true && on == true)
            {
                proceso.StartInfo.FileName = @"C:\Program Files (x86)\IDA\rougue-studios\IDA\scripts\icon.py";
                proceso.Start();
                
            }

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //btnIniciarDetener.Region = Region.FromHrgn(CreateRoundRectRgn(0, 0, btnIniciarDetener.Width, btnIniciarDetener.Height, 20, 20));
//            btnIniciarDetener.Text = "Iniciar";
        }

        private void btnSalir_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
