using System;
using System.Data;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace ClimbingDBApp.App
{
    public partial class MainForm : Form
    {
        private SqlConnection connection;
        private DataSet dataSet;
        private SqlDataAdapter climberDataAdapter;
        private SqlDataAdapter gymDataAdapter;
        private SqlCommandBuilder climberCommandBuilder;
        private BindingSource climberBindingSource;
        private BindingSource gymBindingSource;
        
        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            connection = new SqlConnection(@"Server = localhost,1433; Initial Catalog = ClimbingDB; " +
                                           "User ID=sa; Password=2{#9y*kPgG}KLz]B");
            dataSet = new DataSet();
            climberDataAdapter = new SqlDataAdapter("SELECT * FROM climber", connection);
            gymDataAdapter = new SqlDataAdapter("SELECT * FROM gym", connection);
            climberCommandBuilder = new SqlCommandBuilder(climberDataAdapter);

            climberDataAdapter.Fill(dataSet, "climber");
            gymDataAdapter.Fill(dataSet, "gym");
            
            var climberToGymRelation = new DataRelation(
                "FK_climber_gym_id", dataSet.Tables["gym"].Columns["id"],
                dataSet.Tables["climber"].Columns["gym_id"]);
            dataSet.Relations.Add(climberToGymRelation);

            gymBindingSource = new BindingSource
            {
                DataSource = dataSet, DataMember = "gym"
            };
            climberBindingSource = new BindingSource
            {
                DataSource = gymBindingSource, DataMember = "FK_climber_gym_id",
            };

            gymDataGrid.DataSource = gymBindingSource;
            climberDataGrid.DataSource = climberBindingSource;
        }

        private void updateButton_Click(object sender, EventArgs e)
        {
            climberDataAdapter.Update(dataSet, "climber");
        }
    }
}