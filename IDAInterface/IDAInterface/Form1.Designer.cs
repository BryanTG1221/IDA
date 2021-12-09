namespace IDAInterface
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.btnIniciarDetener = new System.Windows.Forms.Button();
            this.rdbSiempreEscuchando = new IDAInterface.RJRadioButton();
            this.rdbAutomatico = new IDAInterface.RJRadioButton();
            this.rdbManual = new IDAInterface.RJRadioButton();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.btnSalir = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // btnIniciarDetener
            // 
            this.btnIniciarDetener.BackColor = System.Drawing.Color.DodgerBlue;
            this.btnIniciarDetener.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
            this.btnIniciarDetener.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnIniciarDetener.FlatAppearance.BorderSize = 0;
            this.btnIniciarDetener.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnIniciarDetener.Font = new System.Drawing.Font("Segoe UI", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnIniciarDetener.ForeColor = System.Drawing.Color.White;
            this.btnIniciarDetener.Location = new System.Drawing.Point(115, 323);
            this.btnIniciarDetener.Name = "btnIniciarDetener";
            this.btnIniciarDetener.Size = new System.Drawing.Size(85, 23);
            this.btnIniciarDetener.TabIndex = 0;
            this.btnIniciarDetener.Text = "Iniciar";
            this.btnIniciarDetener.UseVisualStyleBackColor = false;
            this.btnIniciarDetener.Click += new System.EventHandler(this.btnIniciarDetener_Click);
            // 
            // rdbSiempreEscuchando
            // 
            this.rdbSiempreEscuchando.AutoSize = true;
            this.rdbSiempreEscuchando.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(84)))), ((int)(((byte)(246)))));
            this.rdbSiempreEscuchando.CheckedColor = System.Drawing.SystemColors.Menu;
            this.rdbSiempreEscuchando.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.rdbSiempreEscuchando.ForeColor = System.Drawing.Color.White;
            this.rdbSiempreEscuchando.Location = new System.Drawing.Point(89, 296);
            this.rdbSiempreEscuchando.MinimumSize = new System.Drawing.Size(0, 21);
            this.rdbSiempreEscuchando.Name = "rdbSiempreEscuchando";
            this.rdbSiempreEscuchando.Padding = new System.Windows.Forms.Padding(10, 0, 0, 0);
            this.rdbSiempreEscuchando.Size = new System.Drawing.Size(134, 21);
            this.rdbSiempreEscuchando.TabIndex = 7;
            this.rdbSiempreEscuchando.Text = "Siempre escuchando";
            this.rdbSiempreEscuchando.UnCheckedColor = System.Drawing.Color.Gray;
            this.rdbSiempreEscuchando.UseVisualStyleBackColor = false;
            // 
            // rdbAutomatico
            // 
            this.rdbAutomatico.AutoSize = true;
            this.rdbAutomatico.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(84)))), ((int)(((byte)(246)))));
            this.rdbAutomatico.CheckedColor = System.Drawing.SystemColors.Menu;
            this.rdbAutomatico.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.rdbAutomatico.ForeColor = System.Drawing.Color.White;
            this.rdbAutomatico.Location = new System.Drawing.Point(89, 269);
            this.rdbAutomatico.MinimumSize = new System.Drawing.Size(0, 21);
            this.rdbAutomatico.Name = "rdbAutomatico";
            this.rdbAutomatico.Padding = new System.Windows.Forms.Padding(10, 0, 0, 0);
            this.rdbAutomatico.Size = new System.Drawing.Size(116, 21);
            this.rdbAutomatico.TabIndex = 6;
            this.rdbAutomatico.Text = "Modo automático";
            this.rdbAutomatico.UnCheckedColor = System.Drawing.Color.Gray;
            this.rdbAutomatico.UseVisualStyleBackColor = false;
            // 
            // rdbManual
            // 
            this.rdbManual.AutoSize = true;
            this.rdbManual.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(84)))), ((int)(((byte)(246)))));
            this.rdbManual.Checked = true;
            this.rdbManual.CheckedColor = System.Drawing.SystemColors.MenuBar;
            this.rdbManual.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.rdbManual.ForeColor = System.Drawing.Color.White;
            this.rdbManual.Location = new System.Drawing.Point(89, 242);
            this.rdbManual.MinimumSize = new System.Drawing.Size(0, 21);
            this.rdbManual.Name = "rdbManual";
            this.rdbManual.Padding = new System.Windows.Forms.Padding(10, 0, 0, 0);
            this.rdbManual.Size = new System.Drawing.Size(98, 21);
            this.rdbManual.TabIndex = 5;
            this.rdbManual.TabStop = true;
            this.rdbManual.Text = "Modo manual";
            this.rdbManual.UnCheckedColor = System.Drawing.Color.Gray;
            this.rdbManual.UseVisualStyleBackColor = false;
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = global::IDAInterface.Properties.Resources.logo;
            this.pictureBox1.Location = new System.Drawing.Point(-95, -92);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(406, 335);
            this.pictureBox1.TabIndex = 8;
            this.pictureBox1.TabStop = false;
            // 
            // btnSalir
            // 
            this.btnSalir.BackColor = System.Drawing.Color.DodgerBlue;
            this.btnSalir.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
            this.btnSalir.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnSalir.FlatAppearance.BorderSize = 0;
            this.btnSalir.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnSalir.Font = new System.Drawing.Font("Segoe UI", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnSalir.ForeColor = System.Drawing.Color.White;
            this.btnSalir.Location = new System.Drawing.Point(115, 352);
            this.btnSalir.Name = "btnSalir";
            this.btnSalir.Size = new System.Drawing.Size(85, 23);
            this.btnSalir.TabIndex = 4;
            this.btnSalir.Text = "Salir";
            this.btnSalir.UseVisualStyleBackColor = false;
            this.btnSalir.Click += new System.EventHandler(this.btnSalir_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSize = true;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(84)))), ((int)(((byte)(246)))));
            this.ClientSize = new System.Drawing.Size(311, 412);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.rdbSiempreEscuchando);
            this.Controls.Add(this.rdbAutomatico);
            this.Controls.Add(this.rdbManual);
            this.Controls.Add(this.btnSalir);
            this.Controls.Add(this.btnIniciarDetener);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "IDA";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnIniciarDetener;
        private RJRadioButton rdbManual;
        private RJRadioButton rdbAutomatico;
        private RJRadioButton rdbSiempreEscuchando;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button btnSalir;
    }
}

