package com.example.cropad;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class first_page extends AppCompatActivity {

    public Button log_out;

    public Button add_market;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_first_page);
        log_out= (Button) findViewById(R.id.logout_but);
        log_out.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent l = new Intent(first_page.this, MainActivity.class);
                startActivity(l);
            }
        });

        add_market = (Button) findViewById(R.id.add_market_but);
        add_market.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent addmkt = new Intent(first_page.this, add_market.class);
                startActivity(addmkt);
            }
        });
    }
}
