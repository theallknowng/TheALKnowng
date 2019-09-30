package com.example.cropad;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.LinearLayout;
import android.widget.ListAdapter;

import java.util.ArrayList;

public class expertadvice extends AppCompatActivity {

    RecyclerView recyclerView;
    ArrayList<expertdata> expertdataList;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_expertadvice);
        recyclerView = findViewById(R.id.expert_advice_recyclerview);

        expertdataList = new ArrayList<>();
        expertdataList.add(new expertdata("alok", "crop"));
        expertdataList.add(new expertdata("alok", "crop"));
        expertdataList.add(new expertdata("alok", "crop"));
        expertdataList.add(new expertdata("alok", "crop"));
        expertdataList.add(new expertdata("alok", "crop"));
        expertdataList.add(new expertdata("alok", "crop"));
        expertdataList.add(new expertdata("alok", "crop"));
        expertdataList.add(new expertdata("alok", "crop"));
        expertdataList.add(new expertdata("alok", "crop"));
        expertdataList.add(new expertdata("alok", "crop"));
        expertdataList.add(new expertdata("alok", "crop"));
        expertdataList.add(new expertdata("alok", "crop"));
        expertdataList.add(new expertdata("alok", "crop"));
        expertdataList.add(new expertdata("alok", "crop"));

        LinearLayoutManager layoutManager = new LinearLayoutManager(getApplicationContext());
        RecyclerView.LayoutManager layoutManager1 = layoutManager;
        ExpertAdapter adapter = new ExpertAdapter(getApplicationContext(), expertdataList);

        recyclerView.setLayoutManager(layoutManager1);
        recyclerView.setAdapter(adapter);

    }
}
