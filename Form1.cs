using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TXTer
{
    public partial class Form1 : Form
    {

        string filename,outdir,outname;

        public Form1()
        {
            InitializeComponent();


        }

        private void button1_Click(object sender, EventArgs e)
        {

            //string filename = selectfile();

            //string out_dir = @"C:\Users\zym79\Downloads\";
            //string out_name = "1.txt";

            if (outdir == null)
            {
                MessageBox.Show("请选择输出目录！");
                return;
            }


            if (filename == null)
            {
                MessageBox.Show("请选择TXT文件！");
                return ;

            }
            string[] getAry = filename.Split('\\');

            outname = getAry[getAry.Length-1];

            string o = outdir + "\\" + outname;
            string order= "jiantofan.exe " + '"'+ @filename+ '"'+" " + '"' + @o+'"';
            string result = cmd(order).Replace("\n", "");
            if (result.Replace("\r", "") == "ok")
            {
                MessageBox.Show("转换完成！");
            }
            else
            {
                MessageBox.Show("转换失败！");
            }
            /*
                        string s = "jiantofan.exe"+jian;




                        string result = cmd(s);

                        MessageBox.Show(result);*/

        }

        //调用命令行
        private string cmd(string order)
        {
            Process p = new Process();
            //设置要启动的应用程序
            p.StartInfo.FileName = "cmd.exe";
            //是否使用操作系统shell启动
            p.StartInfo.UseShellExecute = false;
            // 接受来自调用程序的输入信息
            p.StartInfo.RedirectStandardInput = true;
            //输出信息
            p.StartInfo.RedirectStandardOutput = true;
            // 输出错误
            p.StartInfo.RedirectStandardError = true;
            //不显示程序窗口
            p.StartInfo.CreateNoWindow = true;
            //启动程序
            p.Start();

            //向cmd窗口发送输入信息
            p.StandardInput.WriteLine(order + "&exit");

            p.StandardInput.AutoFlush = true;

            //获取输出信息
            string strOuput = p.StandardOutput.ReadToEnd();
            //等待程序执行完退出进程
            p.WaitForExit();
            p.Close();

            string[] s = strOuput.Split('\n');

            

            return s[4];

        }
        
        //选择文件
        private string selectfile()
        {
            //使用OpenDialog
            OpenFileDialog dialog = new OpenFileDialog();

            dialog.Multiselect = false;//只选择单个文件
            dialog.Title = "请选择文件";
            dialog.Filter = "TXT文件(*.txt)|*.txt";//选择某种类型的文件
            if (dialog.ShowDialog() == DialogResult.OK)
            {
                string filename = dialog.FileName;
                return filename;
            }
            return null;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (outdir == null)
            {
                MessageBox.Show("请选择输出目录！");
                return;
            }


            if (filename == null)
            {
                MessageBox.Show("请选择TXT文件！");
                return;

            }
            string[] getAry = filename.Split('\\');

            outname = getAry[getAry.Length - 1];

            string o = outdir + "\\" + outname;
            string order = "fantojian.exe " + '"' + @filename + '"' + " " + '"' + @o + '"';
            string result = cmd(order).Replace("\n","");
            if(result.Replace("\r","") == "ok")
            {
                MessageBox.Show("转换完成！");
            }
            else
            {
                MessageBox.Show("转换失败！");
            }
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            filename=selectfile();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            FolderBrowserDialog folder = new FolderBrowserDialog();
            folder.Description = "选择输出目录";  //提示的文字
            if (folder.ShowDialog() == DialogResult.OK)
            {
                outdir = folder.SelectedPath;
            }
        }
    }
}
