/**
 * \file wxTest.cpp
 * \brief Programa de ejemplo para probar la compilación con wxWidgets.
 *
 * Ejecutar `make` y verificar que el programa compila y corre bien.
 */

#include <iostream>
#include <vector>
#include <wx/app.h>
#include <wx/frame.h>
#include <wx/sizer.h>
#include <wx/stattext.h>

/**
 * \class Test
 * \brief Clase de ejemplo que implementa `wxApp`.
 */
class Test : public wxApp {
private:

public:
	virtual bool OnInit();
	virtual int OnExit();
};

IMPLEMENT_APP(Test)

/**
 * \brief Función al salir. Debe devolver 0.
 */
int Test::OnExit()
{
	return 0;
}

/**
 * \brief Función principal, inicio del programa.
 */
bool Test::OnInit()
{
	wxFrame *mainWindow = new wxFrame(NULL, wxID_ANY, "Hola");
	mainWindow->SetSize(300, 200);
	
	wxBoxSizer *sizer = new wxBoxSizer(wxVERTICAL);
	sizer->Add(new wxStaticText(mainWindow, -1, "Compila bien!!!"),
		0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5);
	mainWindow->SetSizer(sizer);
	
	mainWindow->Centre();
	mainWindow->Show();
	
	return true;
}
