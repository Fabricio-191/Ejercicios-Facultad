package fabricio.rubio.proyecto.moea.persistence.entities;

import org.moeaframework.core.Variable;
import org.moeaframework.util.validate.Validate;

import java.io.Serializable;
import java.util.Formattable;
import java.util.HashMap;
import java.util.Map;

public class Solution implements Formattable<Solution>, Serializable {
    private static final long serialVersionUID = 1L;
    private final Variable[] variables;
    private final double[] objectives;
    private final double[] constraints;
    private final Map<String, Serializable> atributes;

    public Solution(int numberOfVariables, int numberOfObjectives, int numberOfConstraints) {
        Validate.that("numberOfVariables", numberOfVariables).isGreaterThan(0);
		Validate.that("numberOfObjectives", numberOfObjectives).isGreaterThan(0);
		Validate.that("numberOfConstraints", numberOfConstraints).isGreaterThan(0);
        variables = new Variable[numberOfVariables];
        objectives = new double[numberOfObjectives];
        constraints = new double[numberOfConstraints];
        atributes = new HashMap<String, Serializable>();
    }
}
