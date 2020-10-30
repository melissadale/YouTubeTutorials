import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.SWT;
import org.eclipse.wb.swt.SWTResourceManager;
import org.eclipse.swt.widgets.Text;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.events.MouseAdapter;
import org.eclipse.swt.events.MouseEvent;

public class MyAddingCalc {

	protected Shell shell;
	private Text input1_txt;
	private Text input2_txt;

	/**
	 * Launch the application.
	 * @param args
	 */
	public static void main(String[] args) {
		try {
			MyAddingCalc window = new MyAddingCalc();
			window.open();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Open the window.
	 */
	public void open() {
		Display display = Display.getDefault();
		createContents();
		shell.open();
		shell.layout();
		while (!shell.isDisposed()) {
			if (!display.readAndDispatch()) {
				display.sleep();
			}
		}
	}

	/**
	 * Create contents of the window.
	 */
	protected void createContents() {
		shell = new Shell();
		shell.setSize(717, 654);
		shell.setText("SWT Application");
		shell.setLayout(new GridLayout(5, false));
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		
		Label input1_lbl = new Label(shell, SWT.NONE);
		input1_lbl.setFont(SWTResourceManager.getFont("Segoe UI", 30, SWT.NORMAL));
		input1_lbl.setText("Input 1: ");
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		
		input1_txt = new Text(shell, SWT.BORDER);
		input1_txt.setFont(SWTResourceManager.getFont("Segoe UI", 30, SWT.NORMAL));
		input1_txt.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, true, false, 1, 1));
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		
		Label input2_lbl = new Label(shell, SWT.NONE);
		input2_lbl.setText("Input 2: ");
		input2_lbl.setFont(SWTResourceManager.getFont("Segoe UI", 30, SWT.NORMAL));
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		
		input2_txt = new Text(shell, SWT.BORDER);
		input2_txt.setFont(SWTResourceManager.getFont("Segoe UI", 30, SWT.NORMAL));
		input2_txt.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, true, false, 1, 1));
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		
		Button add_btn = new Button(shell, SWT.NONE);

		add_btn.setForeground(SWTResourceManager.getColor(102, 51, 255));
		add_btn.setFont(SWTResourceManager.getFont("Segoe UI", 30, SWT.BOLD));
		add_btn.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, false, false, 1, 1));
		add_btn.setText("ADD");
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		new Label(shell, SWT.NONE);
		
		Label answer_lbl = new Label(shell, SWT.NONE);
		answer_lbl.setForeground(SWTResourceManager.getColor(0, 153, 51));
		answer_lbl.setFont(SWTResourceManager.getFont("Segoe UI", 30, SWT.BOLD));
		answer_lbl.setAlignment(SWT.CENTER);
		answer_lbl.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, false, false, 1, 1));
		answer_lbl.setText("0.0");

		add_btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseDown(MouseEvent e) {
				int given1 = Integer.parseInt(input1_txt.getText());
				int given2 = Integer.parseInt(input2_txt.getText());
				
				int results = given1 + given2;
				
				answer_lbl.setText(Integer.toString(results));
				
			}
		});
		
	}

}
