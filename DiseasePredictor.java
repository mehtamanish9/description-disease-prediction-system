import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;
import org.json.*;

public class DiseasePredictor extends JFrame {

    private JComboBox<String> diseaseBox;
    private JPanel inputPanel;
    private JButton predictBtn;
    private JTextArea resultBox;

    // Define diseases and feature counts (match your Python config)
    private String[] diseases = {
        "Diabetes", "Asthma", "Arthritis", "COPD",
        "Dengue", "Anemia", "Alzheimers"
    };

    // Example feature names (simplified)
    private String[][] features = {
        {"Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"},
        {"Age","Gender","Wheezing","Shortness_of_Breath","Chest_Tightness","Coughing","Night_Symptoms","Exercise_Induced","Family_History"},
        {"Age","Gender","Joint_Pain","Stiffness","Swelling","Redness","Range_of_Motion_Loss"},
        {"Age","Smoking_Years","Packs_Per_Day","Shortness_of_Breath","Chronic_Cough","Sputum_Production","Wheezing"},
        {"Fever_Days","Body_Temperature","Platelet_Count","Hematocrit","WBC_Count","Muscle_Pain","Eye_Pain","Vomiting"},
        {"Gender","Hemoglobin","MCH","MCHC","MCV","Platelet_Count"},
        {"Age","Gender","MMSE","CDR","eTIV","nWBV","ASF"}
    };

    private JTextField[] inputFields;

    public DiseasePredictor() {
        setTitle("Disease Prediction System");
        setSize(600, 650);
        setLayout(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JLabel title = new JLabel("Multi-Disease Prediction System");
        title.setBounds(130, 10, 400, 30);
        title.setFont(new Font("Arial", Font.BOLD, 18));
        add(title);

        JLabel chooseLabel = new JLabel("Select Disease:");
        chooseLabel.setBounds(30, 60, 150, 25);
        add(chooseLabel);

        diseaseBox = new JComboBox<>(diseases);
        diseaseBox.setBounds(150, 60, 300, 25);
        add(diseaseBox);

        inputPanel = new JPanel();
        inputPanel.setBounds(30, 100, 520, 330);
        inputPanel.setLayout(new GridLayout(20, 2));
        add(inputPanel);

        diseaseBox.addActionListener(e -> loadInputs());

        predictBtn = new JButton("Predict");
        predictBtn.setBounds(200, 450, 150, 40);
        add(predictBtn);

        resultBox = new JTextArea();
        resultBox.setBounds(30, 510, 520, 100);
        resultBox.setEditable(false);
        add(resultBox);

        loadInputs();

        predictBtn.addActionListener(e -> predictDisease());
    }

    private void loadInputs() {
        inputPanel.removeAll();
        int index = diseaseBox.getSelectedIndex();
        String[] fs = features[index];

        inputFields = new JTextField[fs.length];

        for (int i = 0; i < fs.length; i++) {
            inputPanel.add(new JLabel(fs[i] + ": "));
            inputFields[i] = new JTextField();
            inputPanel.add(inputFields[i]);
        }

        inputPanel.revalidate();
        inputPanel.repaint();
    }

    private void predictDisease() {
        try {
            int index = diseaseBox.getSelectedIndex();
            String disease = diseases[index];

            JSONArray dataArr = new JSONArray();

            for (JTextField tf : inputFields) {
                dataArr.put(Double.parseDouble(tf.getText()));
            }

            JSONObject json = new JSONObject();
            json.put("disease", disease);
            json.put("data", dataArr);

            URL url = new URL("http://127.0.0.1:5000/predict");
            HttpURLConnection con = (HttpURLConnection) url.openConnection();

            con.setRequestMethod("POST");
            con.setRequestProperty("Content-Type", "application/json");
            con.setDoOutput(true);

            OutputStream os = con.getOutputStream();
            os.write(json.toString().getBytes());
            os.flush();

            BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String response = in.readLine();
            JSONObject res = new JSONObject(response);

            int prediction = res.getInt("prediction");
            double probability = res.getDouble("probability");

            resultBox.setText(
                    "Prediction: " + (prediction == 1 ? "HIGH RISK" : "LOW RISK") +
                    "\nProbability: " + (probability * 100) + "%"
            );

        } catch (Exception ex) {
            resultBox.setText("Error: " + ex.getMessage());
            ex.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new DiseasePredictor().setVisible(true);
    }
}
