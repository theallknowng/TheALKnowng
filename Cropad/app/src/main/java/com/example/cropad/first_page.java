package com.example.cropad;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.ViewFlipper;
import java.text.SimpleDateFormat;
import java.util.Date;

public class first_page extends AppCompatActivity {

    public Button log_out;
    ViewFlipper v_flip;

    public Button add_market;
    public Button weather;
    public Button inputform;

    public void flipperimage(int image){
        ImageView imgview =new ImageView(this);
        imgview.setBackgroundResource(image);
        v_flip.addView(imgview);
        v_flip.setFlipInterval(4000);
        v_flip.setAutoStart(true);

        v_flip.setInAnimation(this,android.R.anim.slide_in_left);
        v_flip.setOutAnimation(this,android.R.anim.slide_out_right);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_first_page);

        SimpleDateFormat sdf = new SimpleDateFormat("MM");
        String currentmonth = sdf.format(new Date());
        Integer currentmonthin = Integer.valueOf(currentmonth);

        int rabi[] = {R.drawable.jowar, R.drawable.wheat};
        int kharif[] = {R.drawable.sugar,R.drawable.jowar};

        v_flip = findViewById(R.id.flipper);

        if (currentmonthin >= 04 && currentmonthin <= 10)
        {
            for (int i = 0; i < rabi.length; i++) {
                flipperimage(rabi[i]);
            }

        }

        else{
            for (int i = 0; i < kharif.length; i++) {
                flipperimage(kharif[i]);
            }

        }

        inputform = (Button) findViewById(R.id.input_form_but);
        inputform.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent input = new Intent(first_page.this , Inputform.class);
                startActivity(input);
            }
        });

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

        weather = (Button) findViewById(R.id.weather);
        weather.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent weather_i = new Intent( first_page.this , weather_forecast.class);
                startActivity(weather_i);
            }
        });
    }
}
