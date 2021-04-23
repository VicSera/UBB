using System;
using System.Data;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.Configuration;

namespace ClimbingDBApp.App
{
    public partial class MainForm : Form
    {
        private SqlConnection connection;
        private DataSet dataSet;
        private SqlDataAdapter childDataAdapter;
        private SqlDataAdapter parentDataAdapter;
        private SqlCommandBuilder commandBuilder;
        private BindingSource childBindingSource;
        private BindingSource parentBindingSource;

        private string parentTableName;
        private string childTableName;
        private string parentTablePK;
        private string childTableFK;
        private string foreignKeyName;
        
        public MainForm()
        {
            InitializeComponent();

            parentTableName = ConfigurationManager.AppSettings.Get("parentTableName");
            childTableName = ConfigurationManager.AppSettings.Get("childTableName");
            parentTablePK = ConfigurationManager.AppSettings.Get("parentTablePK");
            childTableFK = ConfigurationManager.AppSettings.Get("childTableFK");
            foreignKeyName = ConfigurationManager.AppSettings.Get("foreignKeyName");
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            connection = new SqlConnection(@"Server = localhost,1433; Initial Catalog = ClimbingDB; " +
                                           "User ID=sa; Password=2{#9y*kPgG}KLz]B");
            dataSet = new DataSet();
            childDataAdapter = new SqlDataAdapter($"SELECT * FROM {childTableName}", connection);
            parentDataAdapter = new SqlDataAdapter($"SELECT * FROM {parentTableName}", connection);
            commandBuilder = new SqlCommandBuilder(childDataAdapter);

            childDataAdapter.Fill(dataSet, childTableName);
            parentDataAdapter.Fill(dataSet, parentTableName);
            
            var relation = new DataRelation(
                foreignKeyName, dataSet.Tables[parentTableName].Columns[parentTablePK],
                dataSet.Tables[childTableName].Columns[childTableFK]);
            dataSet.Relations.Add(relation);

            parentBindingSource = new BindingSource
            {
                DataSource = dataSet, DataMember = parentTableName
            };
            childBindingSource = new BindingSource
            {
                DataSource = parentBindingSource, DataMember = foreignKeyName,
            };

            gymDataGrid.DataSource = parentBindingSource;
            climberDataGrid.DataSource = childBindingSource;
        }

        private void updateButton_Click(object sender, EventArgs e)
        {
            childDataAdapter.Update(dataSet, childTableName);
        }
    }
}