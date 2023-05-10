from typing import Any, Type

from manim import *
from manim_slides import Slide


def tex_append_animation(tex: Tex, *strings: str, return_new_tex: bool = False):
    new_tex = Tex(
        *tex.tex_strings, *strings, tex_environment=tex.tex_environment
    ).move_to(tex)
    if return_new_tex:
        return TransformMatchingTex(tex, new_tex), new_tex
    return TransformMatchingTex(tex, new_tex)


def animate_submobjects(
    mobject: Mobject,
    AnimClass: Type[Animation],
    animation_options: dict[str, Any] = {},
    group_options: dict[str, Any] = {},
    **kwargs,
):
    return AnimationGroup(
        *(AnimClass(i, **animation_options) for i in mobject), **group_options, **kwargs
    )


class Intro(Slide):
    """
    풀이 개요
    문제 소개
    의도된 풀이
    """

    def construct(self):
        # <Title>
        title = Group(
            Text("미적분을 활용한").scale(1.5),
            Text("확률과 통계 문제 풀이").scale(1.5),
            Text("30301 김건우").scale(0.8),
        ).arrange_in_grid(
            col_alignments="c",
            row_alignments="ccc",
            row_heights=[None, None, 1.5],
            flow_order="dr",
        )
        self.add(title)
        self.wait()
        self.next_slide()

        # <Overview>
        self.clear()
        self.wait()
        self.next_slide()

        overview_text = Text("Overview").scale(1).center().shift(UP * 3)

        overview_rectangle_style = (WHITE, 2.5, 4.5)
        overview_imgs = (
            Group(
                Rectangle(*overview_rectangle_style).add(
                    Tex(
                        r"0 \cdot 4 + 1 \cdot 0 + 2 \cdot 4 \rightarrow {_8C_4 \cdot _4C_0 \cdot _4C_4} \\ "
                        r"0 \cdot 3 + 1 \cdot 2 + 2 \cdot 3 \rightarrow {_8C_3 \cdot _5C_2 \cdot _3C_3} \\ "
                        r"0 \cdot 2 + 1 \cdot 4 + 2 \cdot 2 \rightarrow {_8C_2 \cdot _6C_4 \cdot _2C_2} \\ "
                        r"\vdots",
                        tex_environment="gather*",
                    ).scale(0.5)
                ),
                Rectangle(*overview_rectangle_style).add(
                    MathTex(
                        r"&f(x) = (1+x+x^2)^8 \\ "
                        r"=& \; c_0 + c_1 \cdot x + c_2 \cdot x^2 + \cdots  \\ "
                        r"&+ c_8 \cdot x^8 + \cdots + c_{16} \cdot x^{16}",
                    ).scale(0.65)
                ),
                Rectangle(*overview_rectangle_style).add(
                    MathTex(
                        r"c_8 =& {1 \over n}{\sum^{n-1}_{k=0} f(e^{2 k \pi i k \over n})e^{- 8 \cdot {2 k \pi i k \over n}}} \\"
                        r"=& {1 \over n}{\sum^{n-1}_{k=0} (1 + 2\cos{2 k \pi \over n})^8}",
                    ).scale(0.6)
                ),
                Rectangle(*overview_rectangle_style).add(
                    MathTex(
                        r"&\lim_{n \to \infty} {1 \over n}{\sum^{n-1}_{k=0} (1 + 2\cos{2 k \pi \over n})^8} \\ "
                        r"=& \sum^{8}_{k=0} {_8C_k} 2^k \int^1_0 \cos^k{2 \pi x} \> dx ",
                    ).scale(0.6)
                ),
            )
            .arrange_in_grid(
                buff=(1, 0.5),
                col_alignments="cc",
                row_alignments="cc",
                flow_order="rd",
            )
            .shift(DOWN * 0.7)
        )

        # TODO Add highlights and animations

        # Highlight a_8
        overview_imgs[1].submobjects[0][0][33:35].set_color(color=BLUE)
        overview_imgs[2].submobjects[0][0][0:2].set_color(color=BLUE)

        self.add(overview_text)
        self.add(overview_imgs)

        self.wait()
        self.next_slide()

        # <Problem introduction>
        self.clear()
        self.wait()
        self.next_slide()

        problem = Group(
            Group(
                Text("8개의 정수"),
                MathTex(r"a_1, a_2, a_3, \cdots , a_8").scale(1.2),
            ).arrange(),
            Group(
                Text("조건:"),
                MathTex(r"a_k \in \{0,1,2\} , \; \sum_{k=1}^8 a_k = 8"),
            ).arrange(),
            Group(
                Text("모든 순서쌍 "),
                MathTex(r"(a_1, a_2, a_3, \cdots , a_8)"),
                Text("의 수는?"),
            ).arrange(),
        ).arrange(DOWN, buff=0.75)

        self.play(
            AnimationGroup(
                *[Create(text) for text in problem[0]], lag_ratio=1, run_time=0.3
            )
        )
        self.wait()
        self.next_slide()
        self.play(
            AnimationGroup(
                *[Create(text) for text in problem[1]], lag_ratio=1, run_time=0.3
            )
        )
        self.wait()
        self.next_slide()
        self.play(
            AnimationGroup(
                *[Create(text) for text in problem[2]], lag_ratio=1, run_time=0.3
            )
        )
        self.wait()
        self.next_slide()

        # <Solution>
        self.clear()
        self.wait()
        self.next_slide()

        solution1_1 = MathTex("x")
        solution1_2 = MathTex("x", r", \; ", "y")
        solution1_3 = MathTex("x", r" + 2 ", "y", " = 8")
        self.play(Create(solution1_1), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(
            ReplacementTransform(solution1_1, solution1_2),
            run_time=0.5,
        )
        self.wait()
        self.next_slide()
        self.play(
            TransformMatchingTex(solution1_2, solution1_3),
            run_time=0.5,
        )
        self.wait()
        self.next_slide()

        # Isolate subjects and set key map
        solution2_strings = []
        solution3_strings = []
        solution_key_map = {}
        for i in range(5):
            solution2_strings += [f"({2*i}, ", f"{4-i}) ", r"\quad "]
            solution3_strings += [f"_8C_{2*i} ", r"\cdot ", f"_{8-2*i}C_{4-i} ", "+ "]
            solution_key_map[f"({2*i}, "] = f"_8C_{2*i} "
            solution_key_map[f"{4-i}) "] = f"_{8-2*i}C_{4-i} "
        # Remove trailing \quad and +
        solution2_strings.pop()
        solution3_strings.pop()

        solution2 = MathTex(*solution2_strings)
        self.play(solution1_3.animate.shift(UP * 2), run_time=0.5)
        self.play(
            AnimationGroup(
                *(Create(i) for i in solution2),
                lag_ratio=1,
                run_time=2,
            )
        )
        self.play(solution2.animate.shift(UP * 0.4), run_time=0.3)
        self.wait()
        self.next_slide()

        solution3 = MathTex(*solution3_strings).shift(DOWN)
        self.play(Transform(solution2[0][1].copy(), solution3[0]))
        self.wait()
        self.next_slide()
        self.play(Transform(solution2[1][0].copy(), solution3[1:3]))
        self.wait()
        self.next_slide()

        transforms = []
        for i in range(1, 5):
            transforms.append(
                Transform(solution2[3 * i][1].copy(), solution3[4 * i - 1 : 4 * i + 1])
            )
            transforms.append(
                Transform(
                    solution2[3 * i + 1][0].copy(), solution3[4 * i + 1 : 4 * i + 3]
                )
            )
        self.play(AnimationGroup(*transforms, lag_ratio=0.3))
        self.wait()
        self.next_slide()

        answer = MathTex("= 1107")
        answer.scale(1.2).next_to(solution3, DOWN, buff=1)
        self.play(Create(answer))
        self.wait()
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()


class Polynomial(Slide):
    """
    문제를 다항식 표현으로 변형
    """

    def construct(self):
        polynomial = MathTex(
            "(1+x+x^2)",
            "^8",
        ).scale(1.5)
        self.play(Create(polynomial))
        self.wait()
        self.next_slide()

        x0_rect = SurroundingRectangle(polynomial[0][1])
        x1_rect = SurroundingRectangle(polynomial[0][3])

        x0_tex = MathTex(
            "x^0",
        ).scale(1.3)
        x1_tex = MathTex(
            "x^1",
        ).scale(1.3)

        x0_tex.next_to(polynomial[0][1], DOWN * 1.2)
        x1_tex.next_to(polynomial[0][3], DOWN * 1.2)

        self.play(
            AnimationGroup(
                Create(x0_rect),
                Create(x0_tex),
                lag_ratio=0.5,
                run_time=0.7,
            )
        )
        self.play(FadeOut(x0_rect))
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                Create(x1_rect),
                Create(x1_tex),
                lag_ratio=0.5,
                run_time=0.7,
            )
        )
        self.play(FadeOut(x1_rect))
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                Indicate(x0_tex[0][1]),
                Indicate(x1_tex[0][1]),
                Indicate(polynomial[0][6]),
                lag_ratio=0.5,
            ),
        )
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                Indicate(polynomial[1][0]),
                FadeOut(x0_tex, x1_tex),
                lag_ratio=0.3,
            )
        )
        self.wait()
        self.next_slide()

        expansion1 = MathTex(
            "(1+x+x^2)",
            "(1+x+x^2)",
            r"\cdots",
            "(1+x+x^2)",
        ).shift(UP)
        self.play(polynomial.animate.scale(0.8).shift(UP * 1.5))
        self.play(TransformMatchingTex(polynomial, expansion1))
        self.wait()
        self.next_slide()

        a1_choice = MathTex(
            "1",
        )
        arrow1 = Arrow(
            start=UP,
            end=DOWN,
            max_tip_length_to_length_ratio=0.15,
            max_stroke_width_to_length_ratio=10,
        ).scale(0.5)
        a1 = MathTex(
            "a_1 = ",
            "0",
        )
        a1_group = Group(a1_choice, arrow1, a1)
        a1_group.arrange(DOWN)
        a1_group.next_to(expansion1[0][1], DOWN)
        self.play(
            AnimationGroup(
                Indicate(expansion1[0]),
                ReplacementTransform(expansion1[0][1].copy(), a1_choice),
                Create(arrow1),
                Create(a1),
                lag_ratio=0.8,
                run_time=1.5,
            )
        )
        self.wait()
        self.next_slide()

        a2_choice = MathTex(
            "x",
        )
        arrow2 = arrow1.copy()
        a2 = MathTex(
            "a_2 = ",
            "1",
        )
        a2_group = Group(a2_choice, arrow2, a2)
        a2_group.arrange(DOWN)
        a2_group.next_to(expansion1[1][3], DOWN)
        self.play(
            AnimationGroup(
                Indicate(expansion1[1]),
                ReplacementTransform(expansion1[1][3].copy(), a2_choice),
                Create(arrow2),
                Create(a2),
                lag_ratio=0.8,
                run_time=1.5,
            )
        )
        self.wait()
        self.next_slide()

        expansion1_wide = MathTex(
            "(1+x+x^2)",
            "(1+x+x^2)",
            r"\;",
            r"\cdots",
            r"\;",
            "(1+x+x^2)",
        ).shift(UP)
        dots = MathTex(
            r"\cdots",
        )
        dots.next_to(expansion1_wide[3], DOWN)
        dots.match_y(arrow1)

        a8_choice_ = MathTex(
            "x",
        ).set_opacity(0)
        arrow8 = arrow1.copy()
        a8 = MathTex(
            "a_8 = ",
            "1",
        )
        a8_group = Group(a8_choice_, arrow8, a8)
        a8_group.arrange(DOWN)
        a8_group.next_to(expansion1[3][3], DOWN)
        a8_choice = expansion1[3][3].copy()

        self.play(
            AnimationGroup(
                TransformMatchingTex(expansion1, expansion1_wide),
                Create(dots),
                a1_group.animate.next_to(expansion1_wide[0][1], DOWN),
                a2_group.animate.next_to(expansion1_wide[1][3], DOWN),
                AnimationGroup(
                    ReplacementTransform(a8_choice, a8_choice_),
                    Create(arrow8),
                    Create(a8),
                    lag_ratio=0.5,
                    run_time=0.6,
                ),
                a8_choice.animate.next_to(expansion1_wide[5][3], DOWN),
                a8_group.animate.next_to(expansion1_wide[5][3], DOWN),
            )
        )
        self.wait()
        self.next_slide()

        polynomial.shift(UP * 1.5, LEFT * 4)
        choices = [0, 1, 1, 2, 2, 1, 0, 1]
        multiplication = MathTex(
            "1",
            r" \cdot ",
            "x",
            r" \cdot ",
            r" \cdot ".join(["1", "x", "x^2"][i] for i in choices[2:7]),
            r" \cdot ",
            "x",
        )
        a_sum = MathTex(
            "0",
            "+",
            "1",
            "+",
            "+".join(str(i) for i in choices[2:7]),
            "+",
            "1",
        )

        multiplication.next_to(expansion1_wide, DOWN)
        a_sum.match_y(a1)

        self.play(
            AnimationGroup(
                AnimationGroup(
                    TransformMatchingTex(expansion1_wide, polynomial),
                    FadeOut(arrow1, arrow2, arrow8, dots),
                    TransformMatchingShapes(a1_choice, multiplication[0]),
                    TransformMatchingShapes(a2_choice, multiplication[2]),
                    TransformMatchingShapes(a8_choice, multiplication[6]),
                    TransformMatchingShapes(a1, a_sum[0]),
                    TransformMatchingShapes(a2, a_sum[2]),
                    TransformMatchingShapes(a8, a_sum[6]),
                ),
                AnimationGroup(
                    Create(multiplication),
                    Create(a_sum),
                ),
                lag_ratio=0.7,
            )
        )
        self.wait()
        self.next_slide()

        self.play(ApplyWave(multiplication))
        self.wait()
        self.next_slide()
        self.play(ApplyWave(a_sum))
        self.wait()
        self.next_slide()

        anim1, multiplication = tex_append_animation(
            multiplication, f" = x^{sum(choices)}", return_new_tex=True
        )
        anim2, a_sum = tex_append_animation(
            a_sum, f" = {sum(choices)}", return_new_tex=True
        )
        self.play(anim1, anim2)
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                Circumscribe(a_sum[-1][-1]),
                Circumscribe(multiplication[-1][-1]),
                lag_ratio=1,
            )
        )
        self.wait()
        self.next_slide()

        expansion2 = (
            MathTex(
                r"= c_0 + c_1 \cdot x + \cdots + ",
                "c_8",
                r" \cdot x^8 + \cdots + c_{16} \cdot x^{16}",
            )
            .scale(1.2)
            .match_y(polynomial)
            .shift(DOWN * 2)
        )
        self.play(
            AnimationGroup(
                FadeOut(multiplication, a_sum),
                polynomial.animate.shift(DOWN + RIGHT * 0.8),
                Create(expansion2),
                lag_ratio=0.7,
            )
        )
        self.wait()
        self.next_slide()

        self.play(
            Flash(expansion2[1], flash_radius=0.4),
            expansion2[1].animate.set_color(BLUE),
        )
        self.wait()
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()


class ComplexTrigonometry(Slide):
    """
    복소수와 삼각함수 관계
    nth root of unity
    복소수 거듭제곱의 주기성 활용
    """

    def construct(self):
        polynomial = MathTex("f(x) = ax + b")
        self.play(Create(polynomial))
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                Circumscribe(polynomial[0][5]),
                Circumscribe(polynomial[0][8]),
                lag_ratio=0.2,
            )
        )
        self.wait()
        self.next_slide()

        values = Group(
            MathTex("f(", "x_1", ")"),
            MathTex("f(", "x_2", ")"),
        ).arrange(RIGHT, buff=1)
        self.play(
            polynomial.animate.shift(UP),
        )
        self.play(animate_submobjects(values, Create, lag_ratio=0.5, run_time=0.8))
        self.wait()
        self.next_slide()

        coeffs = (
            Group(
                MathTex(
                    r"a = {f(x_1)-f(x_2) \over x_1 - x_2}",
                    substrings_to_isolate=("f(", "x_1", "x_2", ")"),
                ),
                MathTex(
                    r"b = f(x_1) - a x_1",
                    substrings_to_isolate=("f(", "x_1", "x_2", ")"),
                ),
            )
            .arrange(RIGHT, buff=1)
            .shift(DOWN * 0.3)
        )

        self.play(
            TransformMatchingShapes(values[0].copy(), coeffs[1][:4]),
            TransformMatchingShapes(values[0].copy(), coeffs[1][4:]),
            TransformMatchingShapes(values.copy(), coeffs[0][:9]),
            TransformMatchingShapes(values, coeffs[0][9:]),
        )
        self.wait()
        self.next_slide()

        coeffs_new = (
            Group(
                MathTex("a = f(1) - f(0)"),
                MathTex("b = f(0)"),
            )
            .arrange(RIGHT, buff=1)
            .match_y(coeffs)
        )

        self.play(TransformMatchingShapes(coeffs[1], coeffs_new[1]))
        self.wait()
        self.next_slide()

        self.play(TransformMatchingShapes(coeffs[0], coeffs_new[0]))
        self.wait()
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])

        polynomial = MathTex("f(x) = ax^3 + bx^2 + cx + d")
        self.play(FadeIn(polynomial))
        self.wait()
        self.next_slide()

        values = MathTex(
            r"f(-1) &= - a + b - c + d \\ ",
            r"f(0) &= d  \\ ",
            r"f(1) &= a + b + c + d \\ ",
            r"f(2) &= 8a + 4b + 2c + d \\ ",
        ).shift(DOWN)

        coeffs = (
            MathTex(
                r"a &= - {1 \over 6} f(-1) + {1 \over 2} f(0) - {1 \over 2} f(1) + {1 \over 6} f(2) \\ ",
                r"b &= {1 \over 2} f(-1) - f(0) + {1 \over 2} f(1) \\ ",
                r"c &= - {1 \over 3} f(-1) - {1 \over 2} f(0) + f(1) - {1 \over 6} f(2) \\ ",
                r"d &= f(0) \\ ",
            )
            .scale(0.85)
            .shift(RIGHT * 2.8 + DOWN)
        )

        self.play(
            AnimationGroup(
                polynomial.animate.shift(UP * 2),
                animate_submobjects(values, Create, lag_ratio=0.5),
                lag_ratio=0.8,
            )
        )
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                values.animate.shift(LEFT * 3.7).scale(0.9),
                animate_submobjects(coeffs, Create, lag_ratio=0.5),
                lag_ratio=0.8,
            )
        )
        self.wait()
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()

        complex_number = MathTex("a + b i", substrings_to_isolate=" ").scale(1.8)
        self.play(FadeIn(complex_number, scale=0.5))
        self.wait()
        self.next_slide()

        self.play(Indicate(complex_number[0]))
        self.play(Indicate(complex_number[4:]))

        self.wait()
        self.next_slide()

        complex_mult = MathTex(
            "( a + b i )",
            "( c + d i )",
            substrings_to_isolate=" ",
        ).scale(1.4)
        self.play(
            TransformMatchingShapes(complex_number, complex_mult[:11]),
            FadeIn(complex_mult[11:]),
        )
        self.wait()
        self.next_slide()

        complex_mult_result = MathTex(
            "= ( a c - b d ) + ",
            "( a d + b c ) i",
            substrings_to_isolate=" ",
        )
        complex_mult_result.scale(1.4).shift(UP * 0.5)
        self.play(
            complex_mult.animate.shift(UP * 1.5),
            TransformMatchingTex(complex_mult.copy(), complex_mult_result),
        )
        self.wait()
        self.next_slide()

        substitution = MathTex(
            r"a = \cos(\alpha) & ",
            r" \quad ",
            r"c = \cos(\beta) \\ ",
            r"b = \sin(\alpha) &",
            r"  \quad ",
            r"d = \sin(\beta) \\ ",
            substrings_to_isolate=" ",
        )
        substitution.scale(1.4).next_to(complex_mult_result, DOWN, buff=1)
        self.play(animate_submobjects(substitution, Create, lag_ratio=0.1, run_time=1))
        self.wait()
        self.next_slide()

        complex_mult_subs = MathTex(
            r"& ( \cos(\alpha) + i \sin(\alpha) ) ",
            r"( \cos(\beta) + i \sin(\beta) ) \\ ",
            r"= \; & ( \cos(\alpha) \cos(\beta) - \sin(\alpha) \sin(\beta) ) \\ ",
            r"& + i \cdot ( \cos(\alpha) \sin(\beta) + \sin(\alpha) \cos(\beta) )",
            substrings_to_isolate=" ",
        )
        complex_mult_subs.scale(1.2).shift(UP * 0.5)
        complex_mult_subs_result = MathTex(
            r"=\;& \cos ( \alpha + \beta ) + i \sin( \alpha + \beta )",
            substrings_to_isolate=" ",
        )
        complex_mult_subs_result.scale(1.2)

        Group(complex_mult_subs, complex_mult_subs_result).arrange(
            DOWN, center=False, aligned_edge=LEFT
        )

        self.play(
            TransformMatchingTex(complex_mult, complex_mult_subs),
            TransformMatchingTex(complex_mult_result, complex_mult_subs),
            TransformMatchingTex(substitution, complex_mult_subs),
        )
        self.wait()
        self.next_slide()

        # Highlight cos addition
        self.play(Circumscribe(complex_mult_subs[36:45]))
        self.wait()
        self.next_slide()

        # Highlight sin addition
        self.play(Circumscribe(complex_mult_subs[60:69]))
        self.wait()
        self.next_slide()

        self.play(
            animate_submobjects(
                complex_mult_subs_result, Create, lag_ratio=1, run_time=1
            )
        )
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                FadeOut(complex_mult_subs[27:]),
                AnimationGroup(
                    complex_mult_subs[:27].animate.shift(DOWN * 0.7).scale(1.2),
                    complex_mult_subs_result.animate.shift(UP * 0.5).scale(1.2),
                ),
                lag_ratio=0.7,
            )
        )
        self.play(
            AnimationGroup(
                Circumscribe(complex_mult_subs[3:11]),
                Circumscribe(complex_mult_subs[16:23]),
                lag_ratio=0.8,
            )
        )
        self.wait()
        self.next_slide()

        self.play(
            Indicate(complex_mult_subs_result[5:12]),
            Indicate(complex_mult_subs_result[19:25]),
        )
        self.wait()
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()

        plane = ComplexPlane(
            x_range=(-2.4, 2.4, 1),
            y_range=(-1.5, 1.5, 1),
            x_length=12,
            y_length=7.5,
            faded_line_ratio=4,
            axis_config={"include_numbers": True},
        )
        coord_labels = plane.get_coordinate_labels()

        unit_circle = Circle.from_three_points(
            *(plane.n2p(1), plane.n2p(-1), plane.n2p(1j)),
            color=GREEN,
        )

        self.play(FadeIn(plane, coord_labels))
        self.wait()
        self.next_slide()

        self.play(Create(unit_circle))
        self.wait()
        self.next_slide()

        def create_point_on_unit_circle(
            angle: float,
            text: str,
            arc_radius: float,
            color: str,
            angle_text: bool = True,
        ):
            objs = {}
            objs["point"] = unit_circle.point_at_angle(angle)
            objs["circle"] = Circle(0.08, color=color, fill_opacity=1)
            objs["label"] = MathTex(rf"\cos {text} + i \sin {text}")
            objs["label"].scale(0.7).next_to(objs["point"], objs["point"], 0.1)

            objs["path"] = Arc(radius=plane.get_x_unit_size(), angle=angle)
            objs["segment"] = Line(plane.n2p(0), plane.n2p(1))
            objs["arc"] = Arc(
                plane.get_x_unit_size() * arc_radius, angle=angle, color=color
            )

            text_anim = Wait(run_time=0)
            if angle_text:
                objs["text"] = MathTex(text)
                objs["text"].scale(0.6).next_to(
                    plane.n2p(0), unit_circle.point_at_angle(angle / 2), 0.3
                )
                text_anim = Write(objs["text"])

            objs["circle"].move_to(plane.n2p(1)).set_z_index(1)

            self.play(
                AnimationGroup(
                    Create(objs["segment"], run_time=0.5),
                    GrowFromCenter(objs["circle"], run_time=0.5),
                    lag_ratio=0.7,
                )
            )
            self.play(
                AnimationGroup(
                    MoveAlongPath(objs["circle"], objs["path"]),
                    Rotate(objs["segment"], angle=angle, about_point=plane.n2p(0)),
                    Create(objs["arc"]),
                    lag_ratio=0,
                )
            )
            self.play(
                AnimationGroup(
                    text_anim,
                    Flash(
                        objs["point"],
                        line_length=0.1,
                        flash_radius=0.2,
                        line_stroke_width=2,
                    ),
                    Write(objs["label"], run_time=0.8),
                    lag_ratio=0.3,
                )
            )

            displayed_mobjs = []
            for key in "segment circle arc label".split():
                displayed_mobjs.append(objs[key])
            if angle_text:
                displayed_mobjs.append(objs["text"])

            return objs, displayed_mobjs

        alpha = PI / 6
        alpha_objs, alpha_mobjs = create_point_on_unit_circle(
            alpha, r"\alpha", 0.25, RED
        )
        self.wait()
        self.next_slide()

        alpha_x = Line(plane.n2p(0), (alpha_objs["point"][0], 0, 0))
        alpha_x_label = MathTex(r"\cos \alpha").scale(0.7).next_to(alpha_x, DOWN)
        alpha_y = Line((alpha_objs["point"][0], 0, 0), alpha_objs["point"])
        alpha_y_label = MathTex(r"\sin \alpha").scale(0.7).next_to(alpha_y, RIGHT)

        self.play(Create(alpha_x), Write(alpha_x_label))
        self.wait()
        self.next_slide()
        self.play(Create(alpha_y), Write(alpha_y_label))
        self.wait()
        self.next_slide()

        self.play(
            Uncreate(
                VGroup(alpha_x, alpha_x_label, alpha_y, alpha_y_label), run_time=0.6
            )
        )
        self.wait()
        self.next_slide()

        beta = PI * 3 / 4
        beta_objs, beta_mobjs = create_point_on_unit_circle(beta, r"\beta", 0.225, BLUE)
        self.wait()
        self.next_slide()

        angle_sum = alpha + beta
        angle_sum_objs, angle_sum_mobjs = create_point_on_unit_circle(
            angle_sum, r"( \alpha + \beta )", 0.2, PURPLE, False
        )
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(FadeOut(*alpha_mobjs, *beta_mobjs, *angle_sum_mobjs)),
            FadeOut(unit_circle),
            lag_ratio=0.7,
        )
        self.wait()
        self.next_slide()

        # TODO

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()


class ValueToCoeff(Slide):
    """
    다항함수 함숫값 -> 계수 구하기
    """

    def construct(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()


class Integral(Slide):
    """
    적분식 표현, 삼각함수 거듭제곱 적분, 최종 계산 결과
    """

    def construct(self):
        # TODO Highlight equations

        integral = MathTex(r"\int^1_0 \cos^n{2 \pi x} \> dx").scale(1.2)
        integral_calc = MathTex(
            r"I_n &= ",
            r"\int^1_0 \cos^n {2 \pi x} \> dx \\ ",
            r"&= \int^1_0 \{ 1 - \sin^2 {2 \pi x} \} \, \cos^{n-2} {2 \pi x} \> dx \\ ",
            r"&= I_{n-2} - \int^1_0 \cos^{n-2} {2 \pi x} \, \sin^2 {2 \pi x} \> dx \\",
            r"&= I_{n-2} - \bigl[ \sin {2 \pi x} \cdot \{ - {1 \over 2 \pi (n-1)} \, \cos^{n-1} {2 \pi x} \} \bigr]^1_0 \\",
            r"& + \int^1_0 2 \pi \, \cos {2 \pi x} \, \{ - {1 \over 2 \pi (n-1)} \, \cos^{n-1} {2 \pi x} \} \> dx",
        )
        integral_calc.scale(0.8).shift(LEFT * 1.5)
        integral.match_y(integral_calc[0])

        self.play(Write(integral))
        self.wait()
        self.next_slide()

        integral_1 = MathTex(
            r"I_1 = & \int^1_0 \cos {2 \pi x} \> dx \\ ",
            r"= & \bigl[ {1 \over 2 \pi} \sin {2 \pi x} \bigr] ^1 _0 \\ ",
            r"= & 0",
        )
        integral_1.shift(RIGHT * 2.2)

        integral_2 = MathTex(
            r"I_2 = & \int^1_0 \cos^2 {2 \pi x} \> dx \\ ",
            r"= & \int^1_0 {\cos {4 \pi x} + 1 \over 2 } \> dx \\ ",
            r"= & \bigl[ {1 \over 8 \pi} \sin( 4 \pi x) + {1 \over 2} x \bigr] ^1 _0 \\ ",
            r"= & 1 \over 2",
        )
        integral_2.align_to(integral_1, LEFT)

        integral_1_2 = MathTex(r"I_1 = & 0 \\ ", r"I_2 = & 1 \over 2")
        integral_1_2.scale(0.7).shift(UP * 2.6 + RIGHT * 4.5)

        self.play(TransformMatchingShapes(integral, integral_calc[:2]))
        self.wait()
        self.next_slide()

        self.play(Write(integral_1), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(ReplacementTransform(integral_1, integral_1_2[0]), run_time=0.5)
        self.play(Write(integral_2))
        self.wait()
        self.next_slide()

        self.play(ReplacementTransform(integral_2, integral_1_2[1]), run_time=0.6)
        self.wait()
        self.next_slide()

        self.play(integral_calc[:2].animate.shift(UP * 0.5), run_time=0.5)
        integral_calc[2:].shift(UP * 0.5)
        self.play(Write(integral_calc[2]), run_time=0.7)
        self.wait()
        self.next_slide()

        self.play(
            Group(*integral_calc[2][1:4], integral_calc[2][5], *integral_calc[2][15:])
            .animate(lag_ratio=1, run_time=0.5)
            .set_color(BLUE)
        )
        self.wait()
        self.next_slide()

        integral_calc[3][1:5].set_color(BLUE)
        self.play(Write(integral_calc[3]), run_time=0.7)
        self.wait()
        self.next_slide()

        substitution = MathTex(
            r"u = \sin {2 \pi x}, & \quad v' = \sin {2 \pi x} \cos ^{n-2} {2 \pi x} \\ ",
            r"u' = 2 \pi \cos {2 \pi x}, & \quad v = -{1 \over 2 \pi (n-1)} \cos ^{n-1} {2 \pi x}",
        )
        substitution.scale(0.8).next_to(integral_calc[3], DOWN, 1).set_x(0)
        self.play(Write(substitution[0]), run_time=0.7)
        self.wait()
        self.next_slide()

        self.play(Write(substitution[1]), run_time=0.7)
        self.wait()
        self.next_slide()

        substitution_applied = MathTex(
            r"= I_{n-2} - \bigl[ u v \bigr]^1_0 + \int^1_0 u' v \> dx",
        )
        (
            substitution_applied.scale(0.8)
            .next_to(integral_calc[3], DOWN)
            .align_to(integral_calc[4], LEFT)
        )

        substitution.save_state()
        substitution.scale(0.5).shift(RIGHT * 3 + DOWN * 1.2)
        substitution_box = SurroundingRectangle(substitution, GOLD, stroke_width=1)
        substitution.restore()

        self.play(
            AnimationGroup(
                substitution.animate.scale(0.5).shift(RIGHT * 3 + DOWN * 1.2),
                Create(substitution_box),
                lag_ratio=0.7,
                run_time=1,
            )
        )
        self.play(Create(substitution_applied), run_time=0.7)
        self.wait()
        self.next_slide()

        self.play(
            TransformMatchingShapes(substitution_applied, integral_calc[4:6]),
            run_time=0.7,
        )
        self.wait()
        self.next_slide()

        self.play(Circumscribe(integral_calc[4][7:35]))
        self.wait()
        self.next_slide()

        zero = MathTex("0")
        zero.scale(0.8).next_to(integral_calc[4][5])
        integral_results = [
            MathTex(
                r"&= I_{n-2} + \int^1_0 2 \pi ",
                r"\, ",
                r"\cos {2 \pi x} \, ",
                r"\{ - {1 \over 2 \pi (n-1)} ",
                r"\cos^{n-1} {2 \pi x} ",
                r"\} ",
                r"\> dx",
            ),
            MathTex(
                r"&= I_{n-2} ",
                r"+ ",
                r"\int^1_0 ",
                r"2 \pi ",
                r"\{ - {1 \over 2 \pi (n-1)} ",
                r"\} ",
                r"\, ",
                r"\cos {2 \pi x} \, ",
                r"\cos^{n-1} {2 \pi x} ",
                r"\> dx",
            ),
            MathTex(
                r"&= I_{n-2} ",
                r"+ ",
                r"\int^1_0 ",
                r"\{ ",
                r"- ",
                r"{1 \over n-1} ",
                r"\} ",
                r"\, ",
                r"\cos {2 \pi x} \, ",
                r"\cos^{n-1} {2 \pi x} ",
                r"\> dx",
            ),
            MathTex(
                r"&= I_{n-2} ",
                r"- ",
                r"{1 \over n-1} ",
                r"\int^1_0 ",
                r"\cos {2 \pi x} \, ",
                r"\cos^{n-1} {2 \pi x} ",
                r"\> dx",
            ),
            MathTex(
                r"&= I_{n-2} ",
                r"- ",
                r"{1 \over n-1} ",
                r"\int^1_0 ",
                r"\cos^n {2 \pi x} ",
                r"\> dx",
            ),
            MathTex(
                r"&= I_{n-2} ",
                r"- ",
                r"{1 \over n-1} ",
                r"I_n",
            ),
        ]
        for i in integral_results:
            i.scale(0.8).next_to(integral_calc[3], DOWN).align_to(
                integral_calc[3], LEFT
            )

        self.play(ReplacementTransform(integral_calc[4][6:], zero))
        self.play(FadeOut(integral_calc[4][5:], zero), run_time=0.4)
        self.play(
            TransformMatchingShapes(
                VGroup(integral_calc[4][:5], integral_calc[5]),
                integral_results[0],
            ),
            run_time=0.6,
        )
        self.wait()
        self.next_slide()

        self.play(
            TransformMatchingTex(integral_results[0], integral_results[1]),
            run_time=0.5,
        )
        self.wait()
        self.next_slide()

        self.play(
            TransformMatchingTex(integral_results[1], integral_results[2]),
            run_time=0.5,
        )
        self.wait()
        self.next_slide()

        self.play(
            TransformMatchingTex(integral_results[2], integral_results[3]),
            run_time=0.5,
        )
        self.wait()
        self.next_slide()

        self.play(
            TransformMatchingShapes(integral_results[3], integral_results[4]),
            run_time=0.5,
        )
        self.wait()
        self.next_slide()

        self.play(Indicate(integral_results[4][3:]))
        self.wait()
        self.next_slide()

        self.play(Indicate(integral_calc[1]))
        self.wait()
        self.next_slide()

        self.play(
            TransformMatchingShapes(integral_results[4], integral_results[5]),
            run_time=0.5,
        )
        self.wait()
        self.next_slide()

        result_old = integral_results[-1]
        integral_results = [
            MathTex(r"I_n &= I_{n-2} - {1 \over n-1} I_n", substrings_to_isolate=" "),
            MathTex(r"I_n + {1 \over n-1} I_n &= I_{n-2}", substrings_to_isolate=" "),
            MathTex(r"{n \over n-1} I_n &= I_{n-2}", substrings_to_isolate=" "),
            MathTex(r"I_n &= {n-1 \over n} I_{n-2}", substrings_to_isolate=" "),
        ]

        integral_results[0].scale(0.8).align_to(integral_calc, LEFT).match_y(
            integral_calc[0]
        )
        pos = integral_results[0].get_center()

        self.play(
            AnimationGroup(
                FadeOut(integral_calc[1:4], substitution, substitution_box),
                TransformMatchingShapes(
                    VGroup(integral_calc[0], result_old),
                    integral_results[0],
                ),
                lag_ratio=0.7,
                run_time=0.8,
            ),
        )
        self.wait(0.5)
        self.play(integral_results[0].animate.scale(1.25).center())
        self.wait()
        self.next_slide()

        self.remove(integral_calc)
        self.play(
            TransformMatchingTex(integral_results[0], integral_results[1]),
            run_time=0.5,
        )
        self.wait()
        self.next_slide()

        self.play(
            TransformMatchingTex(integral_results[1], integral_results[2]),
            run_time=0.5,
        )
        self.wait()
        self.next_slide()

        self.play(
            TransformMatchingTex(integral_results[2], integral_results[3]),
            run_time=0.5,
        )
        self.wait()
        self.next_slide()

        self.play(integral_results[3].animate.scale(0.8).move_to(pos))
        integral_1_2.generate_target()
        integral_1_2.target.scale(1.25)

        I_3 = MathTex(r"I_3 = 0")
        I_4 = MathTex(r"I_4 = {3 \cdot 1 \over 4 \cdot 2}")
        I_5 = MathTex(r"I_5 = 0")
        I_6 = MathTex(r"I_6 = {5 \cdot 3 \cdot 1 \over 6 \cdot 4 \cdot 2}")
        I_7 = MathTex(r"I_7 = 0")
        I_8 = MathTex(
            r"I_8 = {7 \cdot 5 \cdot 3 \cdot 1 \over 8 \cdot 6 \cdot 4 \cdot 2}"
        )

        VGroup(
            integral_1_2.target[0], I_3, I_5, I_7, integral_1_2.target[1], I_4, I_6, I_8
        ).arrange_in_grid(
            rows=2, col_widths=[2.5] * 4, buff=(0.25, 0.75), cell_alignment=LEFT
        ).center().shift(
            DOWN * 0.5
        )

        self.play(MoveToTarget(integral_1_2))
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                Write(I_3),
                Write(I_5),
                Write(I_7),
                lag_ratio=0.8,
            )
        )
        self.wait()
        self.next_slide()
        self.play(
            AnimationGroup(
                Write(I_4),
                Write(I_6),
                Write(I_8),
                lag_ratio=0.8,
            )
        )
        self.wait()
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()


class Outro(Slide):
    def construct(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()
