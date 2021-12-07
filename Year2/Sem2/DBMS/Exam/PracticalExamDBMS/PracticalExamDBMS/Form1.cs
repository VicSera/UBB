using System;
using System.Data;
using System.Data.SqlClient;
using System.Windows.Forms;

namespace PracticalExamDBMS
{
    public partial class Form1 : Form
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
        
        public Form1()
        {
            InitializeComponent();
            parentTableName = "Student";
            childTableName = "Assignment";
            parentTablePK = "registration_number";
            childTableFK = "student_id";
            foreignKeyName = "FK__Assignmen__stude__2F10007B";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            connection = new SqlConnection(@"Server = localhost,1433; Initial Catalog = PracticalExam; " +
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

            dgvStudents.DataSource = parentBindingSource;
            dgvAssignments.DataSource = childBindingSource;
        }

        private void updateButton_Click(object sender, EventArgs e)
        {
            childDataAdapter.Update(dataSet, childTableName);
        }
    }
}