namespace ClimbingDBApp.App
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }

            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.climberDataGrid = new System.Windows.Forms.DataGridView();
            this.gymDataGrid = new System.Windows.Forms.DataGridView();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.updateButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize) (this.climberDataGrid)).BeginInit();
            ((System.ComponentModel.ISupportInitialize) (this.gymDataGrid)).BeginInit();
            this.SuspendLayout();
            // 
            // climberDataGrid
            // 
            this.climberDataGrid.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.climberDataGrid.Location = new System.Drawing.Point(44, 261);
            this.climberDataGrid.Name = "climberDataGrid";
            this.climberDataGrid.Size = new System.Drawing.Size(240, 150);
            this.climberDataGrid.TabIndex = 0;
            // 
            // gymDataGrid
            // 
            this.gymDataGrid.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.gymDataGrid.Location = new System.Drawing.Point(44, 63);
            this.gymDataGrid.Name = "gymDataGrid";
            this.gymDataGrid.Size = new System.Drawing.Size(240, 150);
            this.gymDataGrid.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.Location = new System.Drawing.Point(44, 235);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(100, 23);
            this.label1.TabIndex = 2;
            this.label1.Text = "Child table";
            // 
            // label2
            // 
            this.label2.Location = new System.Drawing.Point(44, 37);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(100, 23);
            this.label2.TabIndex = 3;
            this.label2.Text = "Parent table";
            // 
            // updateButton
            // 
            this.updateButton.Location = new System.Drawing.Point(332, 63);
            this.updateButton.Name = "updateButton";
            this.updateButton.Size = new System.Drawing.Size(75, 23);
            this.updateButton.TabIndex = 4;
            this.updateButton.Text = "Update";
            this.updateButton.UseVisualStyleBackColor = true;
            this.updateButton.Click += new System.EventHandler(this.updateButton_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.updateButton);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.gymDataGrid);
            this.Controls.Add(this.climberDataGrid);
            this.Name = "MainForm";
            this.Text = "Climbing App";
            this.Load += new System.EventHandler(this.MainForm_Load);
            ((System.ComponentModel.ISupportInitialize) (this.climberDataGrid)).EndInit();
            ((System.ComponentModel.ISupportInitialize) (this.gymDataGrid)).EndInit();
            this.ResumeLayout(false);
        }

        private System.Windows.Forms.Button updateButton;

        private System.Windows.Forms.DataGridView climberDataGrid;
        private System.Windows.Forms.DataGridView gymDataGrid;

        private System.Windows.Forms.Label label2;

        private System.Windows.Forms.Label label1;

        #endregion
    }
}