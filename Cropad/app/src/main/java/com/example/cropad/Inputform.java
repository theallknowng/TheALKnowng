package com.example.cropad;

import androidx.appcompat.app.AppCompatActivity;
import java.text.SimpleDateFormat;
import java.util.Date;
import android.os.Bundle;
import android.widget.EditText;

public class Inputform extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_inputform);

        EditText datecurrent = findViewById(R.id.date);
        SimpleDateFormat sdf =  new SimpleDateFormat("yyyy.MM.dd ");
        String currentdate = sdf.format(new Date());
        datecurrent.setText(currentdate);

    }
}
